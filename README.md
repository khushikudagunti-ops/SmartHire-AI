# 🤖 SmartHire AI

## Multi-Agent Resume Screening and Candidate Evaluation System

### 📌 Overview

SmartHire AI is an AI-powered resume screening and candidate evaluation platform designed to help recruiters automate the hiring process. The system uses multiple AI agents to analyze resumes, extract skills, score candidates against job requirements, evaluate strengths and weaknesses, and generate AI-powered feedback using Google Gemini.

This project demonstrates the practical application of AI agents in recruitment and human resource management.

---

## 🚀 Features

### ✅ Resume Upload Agent

Allows recruiters to upload resumes in PDF format.

### ✅ Resume Parser Agent

Extracts text content from uploaded resumes using PDF processing.

### ✅ Skill Extraction Agent

Identifies technical skills from resume content.

### ✅ Resume Scoring Agent

Compares candidate resumes with a predefined job description and generates a matching score.

### ✅ Candidate Evaluation Agent

Determines candidate strengths and identifies missing skills.

### ✅ Gemini AI Analysis Agent

Generates:

* Professional Summary
* Candidate Strengths
* Candidate Weaknesses
* Improvement Suggestions
* Interview Questions

### ✅ Candidate Ranking Agent

Ranks candidates based on their resume scores.

---

## 🏗 System Architecture

```text
Upload Resume
      ↓
Resume Parser Agent
      ↓
Skill Extraction Agent
      ↓
Resume Scoring Agent
      ↓
Candidate Evaluation Agent
      ↓
Gemini AI Analysis Agent
      ↓
Candidate Ranking Agent
      ↓
Final Candidate Report
```

---

## 🛠 Technologies Used

* Python
* Streamlit
* PDFPlumber
* Google Gemini API
* Git
* GitHub

---

## 📂 Project Structure

```text
SmartHire-AI
│
├── app.py
├── resume_parser.py
├── skill_extractor.py
├── scorer.py
├── candidate_evaluator.py
├── candidate_ranker.py
├── gemini_agent.py
├── README.md
├── requirements.txt
│
├── data
│   └── job_description.txt
│
├── screenshots
│   ├── dashboard.png
│   ├── score.png
│   ├── skills.png
│   └── analysis.png
│
└── venv
```

---

## 📸 Screenshots

### Dashboard

![Dashboard](screenshots/dashboard.png)

### Resume Score

![Resume Score](screenshots/score.png)

### Skills Detection

![Skills Detection](screenshots/skills.png)

### AI Resume Analysis

![AI Resume Analysis](screenshots/analysis.png)

---

## ▶️ How to Run the Project

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/SmartHire-AI.git
```

### Navigate to Project Folder

```bash
cd SmartHire-AI
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python -m streamlit run app.py
```

---

## 🎯 Project Workflow

1. Upload Resume
2. Extract Resume Text
3. Detect Candidate Skills
4. Compare Resume with Job Description
5. Generate Resume Score
6. Evaluate Candidate Strengths and Weaknesses
7. Generate AI Feedback using Gemini
8. Produce Final Candidate Report

---

## 📈 Results

* Automated resume screening process
* Faster candidate evaluation
* AI-powered feedback generation
* Improved recruiter productivity
* Reduced manual effort in hiring

---

## 🔮 Future Enhancements

* Multiple Resume Upload
* Advanced Candidate Ranking
* Recruiter Dashboard
* Job Description Upload Feature
* Resume Recommendation System
* Cloud Deployment

---

## 👩‍💻 Author

Khushi

---

## ⭐ Acknowledgements

This project was developed as part of an AI Capstone Project using Python, Streamlit, and Google Gemini AI.



