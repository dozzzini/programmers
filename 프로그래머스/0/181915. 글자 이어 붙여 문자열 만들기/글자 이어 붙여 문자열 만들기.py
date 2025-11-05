def solution(my_string, index_list):
    answer = ''
    for i in index_list:
        answer = answer + my_string[i]
        print(my_string[i], end='')
    return answer