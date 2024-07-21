def solution(myString, pat):
    answer = 0
    l_string = myString.lower()
    l_pat = pat.lower()
    if l_pat in l_string:
        return 1
    else:
        return 0