def solution(array):
    
    freq_count = 0  # 가장 많은 횟수
    answer = 0    # 최빈값 
    
    for i in array :
        count = 0   # 현재 등장 수
        for j in array :
            if i == j :
                count += 1
        if count > freq_count :
            freq_count = count # 현재 등장 수가 가장 많은 횟수를 넘으면 count가 freq_count가 됨
            answer = i
        elif count == freq_count and i != answer: # 두 값이 같은 횟수로 나옴 / 근데 두 값이 다른 숫자
            answer = -1

    return answer