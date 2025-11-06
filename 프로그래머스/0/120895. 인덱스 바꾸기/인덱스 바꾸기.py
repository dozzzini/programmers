def solution(my_string, num1, num2):
    answer = ''
    # my_string -> 문자열이니까 리스트로 변환
    string_list = list(my_string)
    string_list[num1] , string_list[num2] = string_list[num2] , string_list[num1]
    
    for i in string_list:
        answer += i
        
    return answer
        
    