from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import tool
import os


def create_agents():

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.3,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    research_agent = Agent(
        role="Senior News Researcher",
        goal="Find the latest real news articles from the internet",
        backstory=(
            "You are an investigative journalist who always uses search tools."
            "to gather verified information and sources."
        ),
        tools=[tool],
        allow_delegation=False,
        verbose=True,
        llm=llm
    )

    fact_checker = Agent(
        role="Fact Checker",
        goal="Verify the accuracy of news sources and remove misinformation",
        backstory="You verify credibility of news reports.",
        verbose=True,
        llm=llm
    )

    writer_agent = Agent(
        role="News Writer",
        goal="Write a professional news article using verified sources",
        backstory="You write articles similar to BBC or Reuters.",
        verbose=True,
        llm=llm
    )

    summary_agent = Agent(
        role="News Summarizer",
        goal="Summarize the article in bullet points",
        verbose=True,
        llm=llm
    )

    return research_agent, fact_checker, writer_agent, summary_agent
