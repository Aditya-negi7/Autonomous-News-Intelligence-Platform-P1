import streamlit as st
import asyncio
from main import run_crew

try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

st.set_page_config(
    page_title="News Intelligence AI",
    layout="wide",
    page_icon="🤖"
)

st.title("🤖 Autonomous News Intelligence Platform")

st.markdown(
"""
A **Multi-Agent AI System** that researches, verifies and writes news automatically.
"""
)

st.sidebar.header("Controls")

topic = st.sidebar.text_input("Enter News Topic")

generate = st.sidebar.button("🚀 Run AI Agents")

st.divider()

col1, col2 = st.columns([2, 1])

article_container = col1.empty()
agent_log = col2.empty()

if generate and topic:

    with st.spinner("AI Agents Working..."):

        agent_log.write("🔍 Research Agent searching news...")
        agent_log.write("🧠 Fact Checker verifying information...")
        agent_log.write("✍️ Writer generating article...")
        agent_log.write("📄 Summarizer creating TLDR...")

        result = run_crew(topic)

        st.subheader("Generated Article")
        st.markdown(result.raw)
        
        st.divider()
        
        st.subheader("Sources")
        st.markdown(
        """
        Sources are extracted from real-time internet search.
        """
        )

        st.download_button(
            "Download Article",
            result.raw,
            file_name="news_article.md"

        )
