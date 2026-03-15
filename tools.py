## https://serper.dev/

from crewai_tools import SerperDevTool
import os

tool = SerperDevTool(
    api_key=os.getenv("SERPER_API_KEY")
    n_results=10
)
