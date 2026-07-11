import streamlit as st
import requests

st.set_page_config(page_title="Personalized Networking Assistant")

st.title("🤝 Personalized Networking Assistant")

# Store last generated result
if "result" not in st.session_state:
    st.session_state["result"] = None

# ------------------------
# Generate Conversation Starters
# ------------------------

event = st.text_input("Enter Event Description")

if st.button("Generate Conversation Starters"):

    response = requests.get(
        "http://127.0.0.1:8000/generate",
        params={"event": event}
    )

    if response.status_code == 200:

        data = response.json()
        st.session_state["result"] = data

# Display last generated result
if st.session_state["result"]:

    st.subheader("Themes")
    st.write(st.session_state["result"]["themes"])

    st.subheader("Conversation Starters")

    for starter in st.session_state["result"]["conversation_starters"]:
        st.success(starter)

    feedback = st.radio(
        "Was this suggestion useful?",
        ["👍 Yes", "👎 No"]
    )

    if st.button("Submit Feedback"):

        requests.get(
            "http://127.0.0.1:8000/feedback",
            params={
                "event": st.session_state["result"]["event"],
                "user_feedback": feedback
            }
        )

        st.success("Feedback submitted successfully!")

st.divider()

# ------------------------
# Fact Checker
# ------------------------

st.header("Fact Checker")

topic = st.text_input("Enter Topic")

if st.button("Check Fact"):

    response = requests.get(
        "http://127.0.0.1:8000/fact",
        params={"topic": topic}
    )

    if response.status_code == 200:
        st.info(response.json()["fact"])

st.divider()

# ------------------------
# Conversation History
# ------------------------

st.header("Conversation History")

if st.button("View History"):

    response = requests.get("http://127.0.0.1:8000/history")

    if response.status_code == 200:

        history = response.json()

        if history:
            for item in history:
                st.write("### Event")
                st.write(item["event"])

                st.write("Conversation Starters")
                for starter in item["conversation"]:
                    st.write("-", starter)

                st.write("---")
        else:
            st.info("No history available.")

st.divider()

# ------------------------
# Feedback History
# ------------------------

st.header("Feedback History")

if st.button("View Feedback"):

    response = requests.get("http://127.0.0.1:8000/feedback-history")

    if response.status_code == 200:

        feedbacks = response.json()

        if feedbacks:
            for item in feedbacks:
                st.write(f"**Event:** {item['event']}")
                st.write(f"**Feedback:** {item['feedback']}")
                st.write("---")
        else:
            st.info("No feedback available.")