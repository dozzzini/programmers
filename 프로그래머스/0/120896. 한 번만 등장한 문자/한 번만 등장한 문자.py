def solution(s):
    answer = ''
    for i in s :    
        # i가 몇 번 나오는지 count -> 한 번만 나오면 answer 에 i 넣기
        if s.count(i) == 1 :  
            answer += i
            answer_list = sorted(answer) # answer_list -> 리스트 
            # print(type(answer_list)) 
            
            # 다시 result 문자열로 변환
            result = ''
            for a in answer_list :
                result += a
            
    return result