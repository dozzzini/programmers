# 1. 어떤 수를 정하고 그 수랑 비교할 수랑 차이를 구하기
# 2. 비교할 대상(초기값) fix 

def solution(array, n):
    answer = array[0]  
    min_diff = abs(array[0] - n)  

    for i in array:
        diff = abs(i - n)
        if diff < min_diff:  # 더 가까우면(=차이가 작은 값)
            min_diff = diff  # fix 했던 값 변경하고 
            answer = i       # array에 있는 i를 변경
        elif diff == min_diff and i < answer :# 차이가 같은데 그게 초기값보다 작으면 
            answer = i

    return answer