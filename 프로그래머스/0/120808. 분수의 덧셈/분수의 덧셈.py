def solution(numer1, denom1, numer2, denom2):
    numer = (numer1 * denom2) + (numer2 * denom1)
    denom = denom1 * denom2

    # 최대공약수 구하기
    divider = 1
    # 분자랑 분모 중에서 작은 것까지의 범위 내에서
    for i in range(1, min(numer, denom) + 1):
        # 분자랑 분모가 둘 다 i로 나누어떨어지면 
        if numer % i == 0 and denom % i == 0:  
            # i 로 나누어주면 약분 가능 
            divider = i  

    # 약분
    numer //= divider
    denom //= divider

    # 결과 반환
    return [numer, denom]
