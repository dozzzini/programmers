def solution(n):
    # print(type(n))
    str_n = str(n)
    # print(type(str_n))
    # print(str_n)
    str_list = list(str_n)
    str_list.sort(reverse=True)
    # print(str_list)
    answer = int("".join(str_list))
    # print(answer)
    return answer