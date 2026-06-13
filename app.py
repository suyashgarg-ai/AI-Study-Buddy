import streamlit as st
import google.generativeai as genai

# API Key
API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")
st.set_page_config(page_title="AI Study Buddy", page_icon="🤓")

st.title("AI Study Buddy 🤓📚")

# ---------------- AI CHAT ----------------

question = st.text_input("Ask anything")

if st.button("Ask AI"):

    if question:

        try:
            response = model.generate_content(question)
            st.success(response.text)

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Please enter a question.")

# ---------------- QUIZ GENERATOR ----------------

st.markdown("---")

st.subheader("📝 Quiz Generator")

topic = st.text_input("Enter a topic for quiz")

if st.button("Generate Quiz"):

    if topic:

        prompt = f"""
        Create 5 MCQs on {topic}.

        Format:
        Question
        A)
        B)
        C)
        D)

        Then provide the correct answer.
        """

        try:
            response = model.generate_content(prompt)
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Please enter a topic.")
        # ---------------- NOTES GENERATOR ----------------

st.markdown("---")

st.subheader("📚 Study Notes Generator")

notes_topic = st.text_input("Enter a topic for notes")

if st.button("Generate Notes"):

    if notes_topic:

        prompt = f"""
        Create detailed study notes on {notes_topic}.

        Include:
        1. Introduction
        2. Key Concepts
        3. Examples
        4. Important Points
        5. Summary

        Make it easy for students to understand.
        """

        try:
            response = model.generate_content(prompt)
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Please enter a topic.")