def solution(s):
    answer = ''
    s_list = list(map(int, s.split()))

    min_num, max_num = min(s_list), max(s_list)
    answer += str(min_num)
    answer += ' '
    answer += str(max_num)
    return answer