from crewai import Task


def create_tasks(researcher, fact_checker, writer, summarizer):

    research_task = Task(
    description=(
        "Search the internet for the MOST RECENT and IMPORTANT news about {topic}.\n\n"
        
        "STRICT REQUIREMENTS:\n"
        "1. Use the search tool to gather REAL articles.\n"
        "2. Find at least 10 UNIQUE articles.\n"
        "3. Articles MUST come from DIFFERENT reputable sources.\n"
        "4. Focus on news published within the last 7–14 days.\n"
        "5. Include major developments, announcements, conflicts, statistics, or policy decisions.\n"
        "6. Avoid repeating the same website more than twice.\n\n"

        "Preferred sources include:\n"
        "Reuters, BBC, CNN, The Hindu, The Indian Express, Hindustan Times, NDTV, Dainik Bhaskar, "
        "New York Times, India Today,The Economic Times, ESPN (for sports), official government sites.\n\n"

        "Each article must include:\n"
        "Title\n"
        "Source Name\n"
        "Publication Date\n"
        "2–3 sentence Summary\n"
        "URL\n"
    ),

    expected_output=(
        "Provide at least 10 articles using this format:\n\n"
        "Title\n"
        "Source\n"
        "Date\n"
        "Summary\n"
        "URL\n\n"
        "Repeat for all articles."
    ),

    agent=researcher
)        

    fact_check_task = Task(
    description=(
        "Verify the credibility of the collected articles.\n\n"
        
        "Tasks:\n"
        "1. Remove duplicate articles.\n"
        "2. Remove low credibility blogs or unknown websites.\n"
        "3. Ensure articles come from reputable organizations.\n"
        "4. Ensure publication dates are recent.\n"
        "5. Keep at least 10 credible articles.\n"
    ),

    expected_output=(
        "A verified list of credible articles including:\n"
        "Title\nSource\nDate\nURL\n"
    ),

    agent=fact_checker,
    context=[research_task]
)

    write_task = Task(
    description=(
        "Using the verified sources, write a comprehensive news report.\n\n"
        
        "The article should:\n"
        "• Explain the major developments clearly\n"
        "• Provide context and background\n"
        "• Explain the impact of the events\n"
        "• Combine insights from multiple sources\n"
        "• Highlight at least 10 key developments\n"
    ),

    expected_output=(
        "Headline\n\n"
        "Introduction explaining the situation\n\n"
        "Detailed analysis of the major developments\n\n"
        "Conclusion summarizing the overall impact"
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
