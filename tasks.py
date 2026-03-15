from crewai import Task


def create_tasks(researcher, fact_checker, writer, summarizer):

    research_task = Task(
        description=(
            "Search the internet for the LATEST news about {topic}. "
            "You MUST use the search tool to gather real articles. "
            "Find at least 5 recent news articles."
        ),
        expected_output=(
            "Return results in this format:\n\n"
            "1. Title\n"
            "Source\n"
            "Date\n"
            "Summary\n"
            "URL\n\n"
            "Repeat for 5 articles."
        ),
        agent=researcher
    )

    fact_check_task = Task(
        description=(
            "Review the research results and remove any unreliable or outdated sources. "
            "Ensure that all articles are from credible sources such as Reuters, BBC, CNN, ESPN etc."
        ),
        expected_output="Verified list of reliable news articles with URLs.",
        agent=fact_checker
    )

    write_task = Task(
        description=(
            "Write a professional news article using the verified sources. "
            "Cite the sources at the end of the article."
        ),
        expected_output=(
            "Full article including:\n"
            "Headline\n"
            "Introduction\n"
            "Body\n"
            "Conclusion\n\n"
            "Sources:\n"
            "List all URLs"
        ),
        agent=writer
    )

    summary_task = Task(
        description="Summarize the article in 5 bullet points.",
        expected_output="TLDR summary with 5 bullet points.",
        agent=summarizer
    )

    return research_task, fact_check_task, write_task, summary_task
