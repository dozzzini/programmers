def solution(my_string):
    answer = []
    i = 0
    
    while i < len(my_string):
        # 문자열 내에 숫자가 있는 경우
        if my_string[i].isdigit() :
            starting_letter = i 
            # my_string 의 길이 내에서 나오는 애들이 숫자라면
            while i < len(my_string) and my_string[i].isdigit() : 
                # 만약 숫자가 연속되어서 나온다면 이어줘야 함 -> 이어주기
                i = i+1     
            # 연속된 숫자 자체를 정수로 반환해서 추가
            answer.append(int(my_string[starting_letter:i]))
        # 숫자가 아니라면 그냥 넘어감
        else:
            i += 1

    return sum(answer)