def solution(numlist, n):
    for i in range(len(numlist)) :
        for j in range(len(numlist)-1) :
            a = numlist[j]
            b = numlist[j+1]

            # 거리 계산
            d_a = abs(a-n)
            d_b = abs(b-n)
            
            # 거리가 크다면 뒤로
            if d_a > d_b :
                numlist[j], numlist[j+1] = numlist[j+1], numlist[j]
            
            # 거리가 같다면 큰 수가 앞에 
            if d_a == d_b and a<b :
                numlist[j], numlist[j + 1] = numlist[j + 1], numlist[j]
    
    return numlist