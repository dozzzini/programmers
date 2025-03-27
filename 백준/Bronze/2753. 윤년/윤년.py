year = int(input())

# 윤년일 때 1 출력
if year%4==0 and year%100!=0:
    print(1)
elif year%400 == 0:
    print(1)
# 윤년이 아닐 때 0 출력
else:
    print(0)