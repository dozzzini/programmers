# 밀어서 B가 될 수 없다 -> 길이가 다르다

def solution(A,B) :
    answer = -1

    #  될 수 없는 경우
    if len(A) != len(B) :
        return answer   
    
    for i in range(len(A)) :
        if A == B :
            return i    #A와 B가 일치하는 경우 0회 반환
        
        a_last = A[-1]
        A = a_last + A[:-1]  # A의 마지막 문자를 맨 앞으로 이동 
        
    return answer