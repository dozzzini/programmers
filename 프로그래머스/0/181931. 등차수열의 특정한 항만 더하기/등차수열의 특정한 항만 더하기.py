def solution(a, d, included):
    answer = 0
    # included 배열의 인덱스 i 들
    for i in range(len(included)):
        # 등차수열의 k 번째 항 : a + (k-1)d
        # k가 i+1 이니까 a + i*d
        now = a + i*d
        if included[i] == True:
            answer += now
    return answer