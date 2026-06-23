from resume_parser import extract_text
from scorer import score_resume


def rank_resumes(files, job_description):

    candidates = []

    for file in files:

        text = extract_text(file)

        score = score_resume(
            text,
            job_description
        )

        candidates.append({
            "name": file.name,
            "score": score
        })

    candidates.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return candidates