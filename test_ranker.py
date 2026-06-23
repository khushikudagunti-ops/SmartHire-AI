from candidate_ranker import rank_candidates

candidates = [
    {"name": "Resume A", "score": 15},
    {"name": "Resume B", "score": 22},
    {"name": "Resume C", "score": 18}
]

result = rank_candidates(candidates)

for candidate in result:
    print(candidate)