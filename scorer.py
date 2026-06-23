def score_resume(resume_text, jd_text):

    score = 0

    jd_words = jd_text.lower().split()

    resume_text = resume_text.lower()

    for word in jd_words:

        if word in resume_text:

            score += 1

    return score