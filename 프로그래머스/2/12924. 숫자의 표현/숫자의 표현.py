def solution(n):
    answer = 0

    for i in range(1, n+1):
        # print('i',i)
        total = 0 
        while total < n :
            total += i
            i += 1
            # print('total',total)
        # total 이 15가 되는 경우만 다 세어주기
        if total == n :
            answer += 1

    return answer