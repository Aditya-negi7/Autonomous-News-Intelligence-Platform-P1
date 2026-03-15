## https://serper.dev/
from dotenv import load_dotenv
load_dotenv()
import os

from crewai_tools import SerperDevTool


# Initialize the tool for internet searching capabilities

tool = SerperDevTool()
