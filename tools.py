## https://serper.dev/

from crewai_tools import SerperDevTool
import os

search_tool = SerperDevTool(
    api_key=os.getenv("SERPER_API_KEY")
    n_results=10
)

tool = search_tool

