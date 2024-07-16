def solution(myString, pat):
    answer = 0
    # B를 바로 A로 바꿔버리면 replaced 에서 A를 B로 바꿀 때 B에서 A로 바뀐 건지, 아니면 원래 A인지 모르기 때문에
    # 이를 구분하기 위해서 B를 우선 C 로 바꾼다.
    temp = myString.replace('B','C')
    # 그리고 난 후에, A를 B로 바꾸고, C로 바꿨던 것을 A로 바꾼다. 
    replaced = temp.replace('A', 'B').replace('C', 'A')
    # replaced 에 pat이 포함되어 있으면 1을 출력하고
    if pat in replaced:
        result = 1
    # replaced 에 pat이 포함되어 있지 않으면 0을 출력한다. 
    else:
        result = 0
    return result