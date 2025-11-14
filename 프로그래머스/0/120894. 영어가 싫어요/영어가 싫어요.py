# 딕셔너리 만들고
# numbers 를 리스트로 만든 다음에 하나씩 뽑아서 
# key 값이랑 비교 -> 그 key에 해당하는 value 추출

def solution(numbers):
    answer = 0
    num_dict = {'zero':0,
                'one':1, 'two':2,'three':3,'four':4,'five':5, 
                'six':6, 'seven': 7, 'eight':8, 'nine':9}

    temp = ""  # 글자 누적할 변수(o+n+e)

    for ch in numbers:       # 한 글자씩 읽기(ch => o,n,e,t,w,...)
        temp += ch           # 글자 누적
        if temp in num_dict: # 누적된 글자가 key라면(완성된 one, two..)
            answer = answer * 10 + num_dict[temp]   # 자리수 올리고 value 값을 더하기
            temp = ""        # 초기화 (안하면 onetwo이런 식으로 되니까 숫자가 못나옴)
    
    return answer