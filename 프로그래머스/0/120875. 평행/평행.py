def solution(dots):
    x1 = dots[0][0]
    y1 = dots[0][1]
    x2 = dots[1][0]
    y2 = dots[1][1]
    x3 = dots[2][0]
    y3 = dots[2][1]
    x4 = dots[3][0]
    y4 = dots[3][1]

    # 기울기 비교 -> 나눗셈으로 하면 소수점 처리 귀찮아서 곱셈으로
    if (y2 - y1) * (x4 - x3) == (y4 - y3) * (x2 - x1):
        return 1


    if (y3 - y1) * (x4 - x2) == (y4 - y2) * (x3 - x1):
        return 1


    if (y4 - y1) * (x3 - x2) == (y3 - y2) * (x4 - x1):
        return 1
    
    else:
        return 0
