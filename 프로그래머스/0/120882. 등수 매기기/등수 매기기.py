# print(score[0][0]) # 영어점수 
# print(score[0][1]) # 수학점수 

def solution(score):

    avg_list = []

    # 평균 구하기
    for s in range(len(score)):
        avg = (score[s][0] + score[s][1]) / 2
        avg_list.append(avg)

    # 내림차순 정렬    
    sorted_avg_list = sorted(avg_list, reverse=True)

    # 등수 리스트
    rank_list = []

    for a in avg_list:
        rank = sorted_avg_list.index(a) + 1
        rank_list.append(rank)

    return rank_list