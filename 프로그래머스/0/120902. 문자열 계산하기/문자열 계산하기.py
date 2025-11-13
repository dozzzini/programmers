# my_string 은 문자열
# my_string을 공백을 기준으로 분리
# 문자열 -> 정수형

def solution(my_string):
    splited = my_string.split()
    result = int(splited[0])   

    op = None   # 이전 연산자를 저장할 변수 초기화

    for x in splited[1:]:   
        if x == '+' or x == '-': 
            op = x
        else:   # 연산자가 아니다 = 숫자처럼 생긴 문자다 -> 문자로 형 변환 필요
            num = int(x)
            
            if op == '+':
                result += num
            else:
                result -= num

    return result

