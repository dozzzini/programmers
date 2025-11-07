def solution(my_string):
    answer = ''
    lower_string = my_string.lower() # 소문자로 변환(string)
    s_lower_string = sorted(lower_string) # 순서대로 정렬(list)
    
    for i in s_lower_string:
        answer += i
    
    return answer