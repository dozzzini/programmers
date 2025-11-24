def solution(num, total):
    # 가운데 값 구함
    center = total / num  

    # 시작점(start)을 구하기 -> 절반을 왼쪽으로 이동해서 시작점 찾음 
    start = center - (num - 1) / 2  

    return [int(start + i) for i in range(num)]