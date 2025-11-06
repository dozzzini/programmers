def solution(rsp):
    answer = ''
    
    for i in rsp:
        if i == '5':
            answer += '2'

        elif i == '0':
            answer += '5'

        elif i == '2':
            answer += '0'

    return answer