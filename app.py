import streamlit as st
from resume_parser import extract_text
from skill_extractor import extract_skills
from candidate_evaluator import evaluate_candidate
from scorer import score_resume
from gemini_agent import analyze_resume

# Page Configuration
st.set_page_config(
    page_title="SmartHire AI",
    page_icon="🤖",
    layout="wide"
)

# Header
st.title("🤖 SmartHire AI")
st.markdown("---")

st.header("📄 Resume Screening Dashboard")

st.info("""
SmartHire AI uses multiple AI agents to:

• Parse resumes automatically

• Extract candidate skills

• Score resumes against job requirements

• Evaluate strengths and weaknesses

• Generate AI-powered feedback

• Assist recruiters in candidate screening
""")

# Upload Resume
uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    try:

        # Extract Text
        text = extract_text(uploaded_file)

        # Extract Skills
        skills = extract_skills(text)

        # Evaluate Candidate
        strengths, missing = evaluate_candidate(skills)

        # Load Job Description
        with open("data/job_description.txt", "r", encoding="utf-8") as file:
            jd_text = file.read()

        # Score Resume
        score = score_resume(text, jd_text)

        st.success("✅ Resume Uploaded Successfully!")

        # Dashboard Metrics
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Resume Score", score)

        with col2:
            st.metric("Skills Found", len(skills))

        with col3:
            st.metric("Missing Skills", len(missing))

        st.markdown("---")

        # Skills
        st.subheader("🛠 Detected Skills")

        if skills:
            for skill in skills:
                st.write("✅", skill)
        else:
            st.write("No skills detected.")

        # Strengths
        st.subheader("💪 Strengths")

        if strengths:
            for skill in strengths:
                st.write("✅", skill)
        else:
            st.write("No strengths identified.")

        # Missing Skills
        st.subheader("⚠ Missing Skills")

        if missing:
            for skill in missing:
                st.write("❌", skill)
        else:
            st.write("No missing skills.")

        st.markdown("---")

        # Resume Text
        st.subheader("📄 Extracted Resume Text")

        st.text_area(
            "Resume Content",
            text,
            height=250
        )

        st.markdown("---")

        # Gemini AI Analysis
        st.subheader("🤖 AI Resume Analysis")

        if st.button("Analyze Resume with AI"):

            with st.spinner("Analyzing Resume..."):

                ai_result = analyze_resume(text)

                st.write(ai_result)

    except Exception as e:

        st.error(f"Error: {e}")