# 점수 중 최댓값 : M 
# 모든 점수를 score/m * 100 으로 수정

N = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)

mod_scores = []
for score in scores:
    mod_scores.append(score / max_score * 100)

print(sum(mod_scores) / N)
