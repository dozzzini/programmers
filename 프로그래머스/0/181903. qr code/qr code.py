def solution(q, r, code):
    answer = ''
    # q가 3이고 r이 1인 경우 = index의 번호를 3으로 나눴을 때 나머지가 1이다. 
    # = index 번호가 1,4,7... index의 번호 % q = r
    # code의 index 번호가 0일 때 -> 0 q
    # code의 index 번호가 1일 때 -> 1 j ^
    # code의 index 번호가 2일 때 -> 2 n
    # code의 index 번호가 3일 때 -> 0 w
    # code의 index 번호가 4일 때 -> 1 e ^
    # code의 index 번호가 5일 때 -> 2
    # code의 index 번호가 6일 때 -> 0 ... 
    
    for i in range(len(code)):
        if i % q == r:
            answer += code[i]
    return answer