def solution(spell, dic):
    for d in dic:   # sod, eocd, qixm .. 
        
        # 길이가 다르면 spell을 모두 사용하는 것이 불가능
        if len(d) != len(spell):    # len(spell)은 spell 리스트 안에 있는 단어들로 만들 수 있는 글자수
            continue
        
        temp = list(d)     #['s','o','m','d']

        for s in spell:
            if s in temp:
                temp.remove(s) # 만약 spell 에 있는 p,o,s가 sod, eocd .. 에 있으면 s 제거
            else:
                break

        # temp가 비었다면 spell과 완전히 동일한 문자 구성(=spell에 들어있는 모든 단어로 단어를 만듦)
        if len(temp) == 0:
            return 1

    return 2
