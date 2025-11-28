def solution(num):
    # 반복하는 횟수
    answer = 0
    # num이 1이 될 때까지 아래 반복
    while num != 1:  
        if num % 2 == 0 : # 짝수이면 
            num /= 2
        else : # 홀수이면
            num = num*3 + 1
        
        answer += 1
        
        if answer == 500:
            return -1
        
    return answer