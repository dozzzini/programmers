# 합성수 : 약수의 개수가 3개 이상인 경우

def solution(n):
    answer = 0  # 합성수의 개수를 세어서 넣는 변수
    for i in range(1, n+1) :    
        cnt = 0 # i의 약수의 개수를 세어서 넣는 변수
        for j in range(1, i+1) :
            if i % j == 0:  # i를 j로 나눠서 나머지가 0이면 j는 i의 약수
                cnt += 1
        if cnt > 2 :    # 약수가 3개 이상이면 합성수
            answer += 1
    return answer