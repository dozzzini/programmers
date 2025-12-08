def solution(a, b, n):
    answer = 0 # 새로 받은 콜라의 총합

    # 콜라를 바꿔올 수 있는 경우
    while n >= a : 
        rest = n % a    # 바꿔먹고 남은 거 (나중에 다시 합쳐줘야 함)
        n = (n//a)*b    # 마트에 준 빈 병 개수 * 돌려받는 개수
        answer += n 
        n += rest
    return answer