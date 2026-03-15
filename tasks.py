from crewai import Task


def create_tasks(researcher, fact_checker, writer, summarizer):

    research_task = Task(
        description=(
            "Search the internet for the latest news about {topic}. "
            "You MUST use the search tool to gather real articles. "
            "Find at least 10 recent news articles published in the last 7–14 days."
        ),

        expected_output=(
            "Return results in this format:\n\n"
            "Title\n"
            "Source Name\n"
            "Date\n"
            "Short Summary\n"
            "URL\n\n"
            "Repeat for 10 articles."
        ),

        agent=researcher
    )

    fact_check_task = Task(
        description=(
            "Verify the credibility of the sources and remove unreliable ones. "
            "Only allow trusted outlets such as BBC, Reuters, CNN, ESPN, "
            "Bloomberg, Guardian, or official sports boards."
        ),

        expected_output=(
            "A verified list of at least 10 news articles including:\n"
            "Title\nSource Name\nDate\nURL"
        ),

        agent=fact_checker,
        context=[research_task]
    )

    write_task = Task(
        description=(
            "Write a detailed news report summarizing the major developments "
            "about the topic using the verified sources."
        ),

        expected_output=(
            "A professional article including:\n"
            "Headline\n"
            "Introduction\n"
            "Body\n"
            "Conclusion\n\n"
            "Highlight at least 10 key developments."
        ),

        agent=writer,
        context=[fact_check_task]
    )

    summary_task = Task(
        description=(
            "Create a clean summary of the article with at least 10 major "
            "developments.\n\n"
            "Each development must include a clickable link emoji.\n"
            "Format links like this:\n"
            "Development text 🔗(URL)\n\n"
            "Example:\n"
            "India wins ODI series 🔗(https://example.com)\n\n"
            "Do NOT show the raw URL except inside the emoji link."
        ),

        expected_output=(
            "10+ bullet points summarizing the developments.\n\n"
            "Then list the sources separately like:\n"
            "Sources:\n"
            "1. Reuters\n"
            "2. BBC\n"
            "3. ESPN"
        ),

        agent=summarizer,
        context=[write_task]
    )

    return research_task, fact_check_task, write_task, summary_task
