# nCr

def solution(balls, share):
    if share > balls - share:  # 5C3 계산하는 것보다 5C2 계산하는 게 쉬우니까 
        share = balls - share

    result = 1
    for i in range(share):
        result *= (balls - i)   # 분자 계산
        result //= (i + 1)      # 분모 계산 

    return result
