def solution(str1, str2):
    answer = 0
    # str2 안에 str1이 있다면 1,
    # str2 안에 str1이 없다면 0
    if str1 in str2:
        answer = 1
    else:
        answer = 0
    return answer