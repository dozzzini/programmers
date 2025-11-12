# 1. emergency 안에 있는 숫자가 큰 게 1
# 2. 배열 -> 내림차순으로 정렬 sorted(배열, 순서)
# 3. 정렬된 배열의 인덱스 추출 -> answer 에 담기

def solution(emergency):
    answer = []
    sorted_list = sorted(emergency, reverse = True)
    
    for e in emergency:  
        rank = sorted_list.index(e) + 1  
        answer.append(rank)
        
    return answer