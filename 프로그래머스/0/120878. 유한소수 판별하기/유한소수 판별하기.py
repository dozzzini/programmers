# 기약분수 만드는 법
    # 1. 최대한 나누기 
    # 2. 안나눠질 때 분모를 2랑 5로 나누기 (분모가 1이 될 떄까지)

def solution(a,b):
    # a랑 b가 공통으로 나눠지는 숫자(n) 찾아서 기약분수로 만들기
    n = 2
    while n <= min(a,b) :
        if a % n == 0 and b % n == 0: # 둘 다 나누어떨어지는 경우 -> 공통된 약수
            a = a//n
            b = b//n
        else:                         # 안 나눠떨어지면 다음 숫자로 넘어감
            n = n + 1

    while b % 2 == 0 :
        b = b//2
    
    while b % 5 == 0 :
        b = b //5

    if b == 1:
        return 1
    else:
        return 2
