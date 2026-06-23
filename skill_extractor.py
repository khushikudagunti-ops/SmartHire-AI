def extract_skills(text):

    skills_db = [
        "python",
        "java",
        "c",
        "c++",
        "sql",
        "mysql",
        "machine learning",
        "deep learning",
        "power bi",
        "excel",
        "tableau",
        "data analysis",
        "html",
        "css",
        "javascript",
        "git",
        "github",
        "tensorflow",
        "pandas",
        "numpy"
    ]

    found_skills = []

    text = text.lower()

    for skill in skills_db:
        if skill in text:
            found_skills.append(skill)

    return found_skills