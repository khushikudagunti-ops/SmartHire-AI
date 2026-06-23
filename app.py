import streamlit as st
from resume_parser import extract_text
from skill_extractor import extract_skills
from candidate_evaluator import evaluate_candidate
from scorer import score_resume
from gemini_agent import analyze_resume
from multi_resume_ranker import rank_resumes

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
• Rank multiple candidates automatically
""")

# -----------------------------
# SINGLE RESUME ANALYSIS
# -----------------------------

st.header("📄 Single Resume Analysis")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"],
    key="single"
)

if uploaded_file is not None:

    try:

        text = extract_text(uploaded_file)

        skills = extract_skills(text)

        strengths, missing = evaluate_candidate(skills)

        with open(
            "data/job_description.txt",
            "r",
            encoding="utf-8"
        ) as file:

            jd_text = file.read()

        score = score_resume(
            text,
            jd_text
        )

        st.success("✅ Resume Uploaded Successfully!")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Resume Score", score)

        with col2:
            st.metric("Skills Found", len(skills))

        with col3:
            st.metric("Missing Skills", len(missing))

        st.markdown("---")

        st.subheader("🛠 Detected Skills")

        for skill in skills:
            st.write("✅", skill)

        st.subheader("💪 Strengths")

        for skill in strengths:
            st.write("✅", skill)

        st.subheader("⚠ Missing Skills")

        for skill in missing:
            st.write("❌", skill)

        st.markdown("---")

        st.subheader("📄 Extracted Resume Text")

        st.text_area(
            "Resume Content",
            text,
            height=250
        )

        st.markdown("---")

        st.subheader("🤖 AI Resume Analysis")

        if st.button("Analyze Resume with AI"):

            with st.spinner("Analyzing Resume..."):

                ai_result = analyze_resume(text)

                st.write(ai_result)

    except Exception as e:

        st.error(f"Error: {e}")

# -----------------------------
# MULTI RESUME RANKING
# -----------------------------

st.markdown("---")

st.header("🏆 Multi Resume Ranking")

uploaded_files = st.file_uploader(
    "Upload Multiple Resumes",
    type=["pdf"],
    accept_multiple_files=True,
    key="multiple"
)

if uploaded_files:

    try:

        with open(
            "data/job_description.txt",
            "r",
            encoding="utf-8"
        ) as file:

            jd_text = file.read()

        ranked_candidates = rank_resumes(
            uploaded_files,
            jd_text
        )

        st.success("✅ Ranking Generated Successfully!")

        st.subheader("🏆 Candidate Rankings")

        rank = 1

        for candidate in ranked_candidates:

            if rank == 1:
                medal = "🥇"
            elif rank == 2:
                medal = "🥈"
            elif rank == 3:
                medal = "🥉"
            else:
                medal = "🏅"

            st.write(
                f"{medal} Rank {rank}: "
                f"{candidate['name']} "
                f"(Score: {candidate['score']})"
            )

            rank += 1

    except Exception as e:

        st.error(f"Ranking Error: {e}")