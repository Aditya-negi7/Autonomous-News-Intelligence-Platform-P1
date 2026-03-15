from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

load_dotenv()

print("Gemini Key:", os.getenv("GOOGLE_API_KEY"))
print("Serper Key:", os.getenv("SERPER_API_KEY"))

from crew_setup import create_crew


def run_crew(topic):

    crew = create_crew()

    topic_lower = topic.lower()

    # Keywords that trigger recency mode
    recency_keywords = ["latest", "recent", "today", "yesterday", "current", "breaking"]

    recency_mode = any(word in topic_lower for word in recency_keywords)

    today = datetime.now()
    three_days_ago = today - timedelta(days=4)

    result = crew.kickoff(
        inputs={
            "topic": topic,
            "recency_mode": recency_mode,
            "today": today.strftime("%B %d, %Y"),
            "three_days_ago": three_days_ago.strftime("%B %d, %Y")
        }
    )

    return result
