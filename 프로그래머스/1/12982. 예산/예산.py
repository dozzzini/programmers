def solution(d, budget):
    d.sort()

    answer = 0
    for dc in d :
        # 만약 부서의 예산이 전체 예산보다 작으면
        # 전체 예산에서 그 부서의 예산을 빼고 
        # 부서의 개수 +1
        if budget >= dc :
            budget -= dc
            answer += 1
        # 전체 예산을 넘으면 어쩔 수 없지     
        else :
            break

    return answer