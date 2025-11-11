def solution(i, j, k):
    answer = 0
    # 1부터 13까지 k인 1이 6번 등장 
    # -> 1, 10(1), 11(2) , 12(1), 13(1) => 6
    # 1. 숫자 -> 문자로 형 변환
    # 2. 바뀐 문자 안에 k가 있다면 answer + 1
    
    for num in range(i,j+1) : # ex num => 1에서 13
        # print(num) # 1,2,3,4,... 13 출력
        if str(k) in str(num): # 문자열로 바꾸면 '1','2',...'11'
            answer += str(num).count(str(k))  # 각 숫자 안에서 k 등장 횟수를 누적

    return answer