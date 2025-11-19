def solution(dots) :
    dots.sort(reverse=False)

    y2 = dots[1][1]
    y1 = dots[0][1]
    x2 = dots[2][0]
    x1 = dots[0][0]
    sero = y2 - y1
    garo = x2 - x1

    return sero * garo