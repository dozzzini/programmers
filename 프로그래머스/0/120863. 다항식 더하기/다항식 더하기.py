def solution(polynomial):
    splited = polynomial.split('+')
    print('더하기로 split:', splited)

    const = 0   # 숫자항 합
    x1 = 0      # x항 합

    # 항 하나씩 보면서 분류하기
    for i in splited:
        t = i.strip()   

        # x가 들어있다면 x항
        if 'x' in t:
            coef = t.replace('x', '')

            # 계수가 1인 경우에는 공백으로 보이니까 1로 설정
            if coef == '':
                    x1 += 1

            else:
                x1 += int(coef)
        # x가 없으면 상수항
        else:
            const += int(t) 

    result = []
    
    # x항 먼저
    if x1 > 0:
        if x1 == 1:
            result.append('x')
        else:
            result.append(str(x1) + 'x')

    # 상수항
    if const > 0:
        result.append(str(const))
    
    # 합치기
    final = ""

    if len(result) >= 1:
        final = result[0]

    if len(result) == 2:
        final = final + " + " + result[1]

    return final