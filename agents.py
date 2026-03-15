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

    research_agent = Agent(
        role="Global News Research Analyst",

        goal=(
            "Find the most recent and important developments about the topic "
            "from the internet using the search tool. Gather real articles "
            "published within the last 7–14 days."
        ),

        backstory=(
            "You are an investigative journalist who gathers real information "
            "from trusted news organizations such as BBC, Reuters, CNN, ESPN, "
            "The Guardian, Bloomberg, Financial Times, and Associated Press. "
            "You always use the search tool and collect article titles, "
            "publication dates, source names, and URLs."
        ),

        tools=[tool],
        allow_delegation=False,
        verbose=True,
        llm=llm
    )

    fact_checker = Agent(
        role="Senior News Fact Checker",

        goal=(
            "Verify that all articles come from credible sources and are recent. "
            "Remove unreliable websites, duplicates, and outdated information."
        ),

        backstory=(
            "You are a newsroom fact-checking editor responsible for verifying "
            "every source. You only allow trusted publications like Reuters, "
            "BBC, ESPN, CNN, Bloomberg, and official sports boards."
        ),

        allow_delegation=False,
        verbose=True,
        llm=llm
    )

    writer_agent = Agent(
        role="International News Correspondent",

        goal=(
            "Write a comprehensive report summarizing the most important "
            "developments about the topic."
        ),

        backstory=(
            "You are a senior journalist writing detailed global reports. "
            "You combine multiple verified sources into a structured article "
            "that explains the latest developments clearly and professionally."
        ),

        allow_delegation=False,
        verbose=True,
        llm=llm
    )

    summary_agent = Agent(
        role="News Intelligence Analyst",

        goal=(
            "Create a structured summary highlighting the most important "
            "developments and events."
        ),

        backstory=(
            "You produce executive-style intelligence briefings. "
            "You extract the most important updates and present them clearly "
            "with references to their sources."
        ),

        allow_delegation=False,
        verbose=True,
        llm=llm
    )

    return research_agent, fact_checker, writer_agent, summary_agent
