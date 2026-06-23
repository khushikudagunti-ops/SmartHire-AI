def rank_candidates(candidate_scores):

    ranked = sorted(
        candidate_scores,
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked