def evaluate_candidate(skills):

    strengths = []
    missing = []

    required_skills = [
        "python",
        "sql",
        "git",
        "machine learning",
        "pandas",
        "numpy"
    ]

    for skill in required_skills:

        if skill in skills:
            strengths.append(skill)

        else:
            missing.append(skill)

    return strengths, missing