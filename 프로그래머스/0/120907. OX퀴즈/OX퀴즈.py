def solution(quiz):
    answer = []
    for i in range(len(quiz)):
        splited = quiz[i].split()
        num1 = splited[0]
        num2 = splited[2]
        result_num = splited[4]
        op = splited[1]
            
        # 일치하는 경우 -> O 출력
        if op == '+':
            if int(result_num) == int(num1) + int(num2):
                answer.append('O')
            else:
                answer.append('X')
        # 일치하지 않는 경우 -> X 출력
        else :
            if int(result_num) == int(num1) - int(num2) :
                answer.append('O')
            else:
                answer.append('X')

        
    return answer