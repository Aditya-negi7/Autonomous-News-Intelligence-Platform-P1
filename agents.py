from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import tool
import os


def create_agents():

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.2,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    # 1️⃣ NEWS RESEARCHER
    research_agent = Agent(
        role="Senior Global News Research Analyst",

        goal=(
            "Find the MOST RECENT and IMPORTANT news related to the given topic "
            "from the internet using the search tool. Focus on real events, "
            "major announcements, breaking news, and developments from the past 7–14 days."
        ),

        backstory=(
            "You are a senior investigative journalist working for a global newsroom. "
            "Your job is to gather factual, up-to-date information from trusted media "
            "organizations such as BBC, Reuters, CNN, ESPN, Al Jazeera, The Guardian, "
            "Bloomberg, and official press releases. "
            "You ALWAYS use the search tool to find real articles and verify dates. "
            "You focus on major events, key announcements, statistics, controversies, "
            "and developments that people need to know."
        ),

        tools=[tool],

        allow_delegation=False,
        verbose=True,
        llm=llm
    )

    # 2️⃣ FACT CHECKER
    fact_checker = Agent(
        role="Senior Fact-Checking Editor",

        goal=(
            "Verify the credibility of news articles, remove unreliable sources, "
            "and ensure the information is factual, recent, and from trusted outlets."
        ),

        backstory=(
            "You are a professional fact-checking editor in a global newsroom. "
            "You verify every article by checking the source credibility, publication "
            "date, and consistency of information. "
            "You only allow trustworthy outlets such as Reuters, BBC, CNN, ESPN, "
            "The Guardian, Bloomberg, Financial Times, Associated Press, etc. "
            "You remove outdated, opinion-only, or low credibility sources."
        ),

        allow_delegation=False,
        verbose=True,
        llm=llm
    )

    # 3️⃣ NEWS WRITER
    writer_agent = Agent(
        role="International News Correspondent",

        goal=(
            "Write a comprehensive, professional news report summarizing the "
            "latest developments and major events related to the topic."
        ),

        backstory=(
            "You are an experienced international news correspondent who writes "
            "detailed reports similar to those published by BBC, Reuters, and "
            "The New York Times. "
            "You analyze multiple verified sources and combine them into a clear, "
            "engaging article. "
            "Your writing highlights the most important events, key developments, "
            "statistics, expert opinions, and context so that readers understand "
            "the full situation."
        ),

        allow_delegation=False,
        verbose=True,
        llm=llm
    )

    # 4️⃣ SUMMARY ANALYST
    summary_agent = Agent(
        role="News Intelligence Analyst",

        goal=(
            "Provide a concise intelligence-style summary of the major news "
            "developments so readers quickly understand the key points."
        ),

        backstory=(
            "You are a strategic news analyst who creates executive-level briefings "
            "from long reports. "
            "You identify the most important insights, major developments, "
            "trends, and implications from the article and present them "
            "in clear bullet points."
        ),

        allow_delegation=False,
        verbose=True,
        llm=llm
    )

    return research_agent, fact_checker, writer_agent, summary_agent
