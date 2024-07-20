def solution(my_string, alp):
    if alp in my_string:
        upper = alp.upper()
        return my_string.replace(alp,upper)
    else:
        return my_string
    