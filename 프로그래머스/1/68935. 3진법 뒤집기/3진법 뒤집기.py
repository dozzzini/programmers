def solution(n):
    string3 = ''
    while n > 0 :
        string3 = string3 + str(n%3)  
        n = n//3

    # 10진법으로 다시
    result = 0
    for i in range(len(string3)) :
        result += int(string3[i]) * 3**(len(string3)-1-i)

    return result