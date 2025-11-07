def solution(n):
    
    x = 1                    # x는 피자 판의 수
    while (6 * x) % n != 0:  # 나누어 떨어질 때까지 반복 
        x += 1               # 안 나눠떨어지면 한판 추가
    return x
