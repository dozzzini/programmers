def solution(myString):
    answer = []
    splited = myString.split('x')
    print(splited)
    for s in splited:
        answer.append(len(s)) 
    
    return answer