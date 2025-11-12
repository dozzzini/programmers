# 1. array 안에 있는 숫자 -> 문자열로 형 변환
# 2. 문자 7의 개수 count

def solution(array):
    answer = 0

    for num in array :
        answer += str(num).count('7')
            
    return answer