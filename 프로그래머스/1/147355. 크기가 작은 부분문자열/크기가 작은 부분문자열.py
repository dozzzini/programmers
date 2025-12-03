def solution(t, p):
    answer = 0
    p_int = int(p)
    p_len = len(p)
    t_len = len(t)

    for i in range(t_len - p_len + 1) :
        my_string = t[i: i+p_len]
        print(my_string)    # 이때까지는 문자열

        if int(my_string) <= p_int : 
            answer += 1
    return answer