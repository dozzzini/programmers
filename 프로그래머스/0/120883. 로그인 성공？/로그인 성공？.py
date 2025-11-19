def solution(id_pw, db):
    
    # id_pw[0] 과 info[0]이 같다면 return login
    id = id_pw[0]
    pw = id_pw[1]

    for info in db:
        if id == info[0] :  
            if pw == info[1]:   # 아이디 같은 경우
                return 'login'
            else :              # 아이디는 같지만 비번이 틀린 경우
                return 'wrong pw'
    return 'fail'               # 아이디가 아예 없는 경우

