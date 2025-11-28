def solution(n):
    answer = 0
    for i in range(1, n+1) :
        if n % i ==0 :
            # print('약수들:',i)
            answer += i
    return answer