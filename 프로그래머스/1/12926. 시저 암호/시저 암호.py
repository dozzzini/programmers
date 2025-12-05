def solution(s, n):
    answer = ''
    
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
    lower = upper.lower()

    # print('총 알파벳 개수:', len(upper)) >> 26

    for i in s :
        # i 에 있을 수 있는 값 << 소문자, 대문자, 공백

        # 1. 공백인 경우 -> 그냥 공백을 넣기 
        if i == ' ':
            answer += i

        # 2. 대문자인 경우 -> upper 문자열에서 i의 인덱스에서 n만큼 밀고 한번 순환하면 맨 앞으로 가야하니까 26으로 나눈 나머지도 설정
        elif i in upper :
            answer += upper[(upper.index(i)+n)%26] 

        # 3. 소문자인 경우 -> lower 문자열에서 " 
        elif i in lower :
            answer += lower[(lower.index(i)+n)%26]

    
    return answer