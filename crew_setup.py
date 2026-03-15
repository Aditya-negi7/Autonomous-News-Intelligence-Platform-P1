from crewai import Crew
from agents import create_agents
from tasks import create_tasks


def create_crew():

    researcher, fact_checker, writer, summarizer = create_agents()

    research_task, fact_check_task, write_task, summary_task = create_tasks(
        researcher,
        fact_checker,
        writer,
        summarizer
    )

    crew = Crew(
        agents=[researcher, fact_checker, writer, summarizer],
        tasks=[research_task, fact_check_task, write_task, summary_task],
        verbose=True
    )

    return crew