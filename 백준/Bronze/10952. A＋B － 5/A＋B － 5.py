# 계속 입력 받음 
while True:
    # 입력이 한 줄로 받으니까 같이 받고 각각의 변수들 분리
    # map(함수, 반복가능한 데이터)
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break

    print(A+B)