def solution(k, score):
    answer = [] # 발표할 점수
    hall = []   # 명예의 전당에 올릴 거

    for i in score : 
        if len(hall) < k :  # 자리가 남은 경우
            hall.append(i)
        else : 
            if (i>min(hall)):   # 기존 게시판에 있는 점수보다 큰 경우
                hall.remove(min(hall))
                hall.append(i)
        hall.sort()
        answer.append(hall[0])
    return answer