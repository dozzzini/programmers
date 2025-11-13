def solution(n):
    i = 2
    i_list = []
    
    while i <= n:           # 12보다 작은 i (2,3,4,~11)
        if n % i == 0:      # 12 % 2 == 0 (나눠떨어짐) -> 소인수
            i_list.append(i) 
            n /= i          
        else:
            i += 1
    
    result = list(set(i_list)) # set으로 중복 제거 후 리스트로 다시 넣음
    
    return sorted(result)
