x = int(input())
y = int(input())

#1사분면에 속하는 경우: x+ y+
if x>0 and y>0:
    print(1)
#2사분면에 속하는 경우: x- y+
elif x<0 and y>0:
    print(2)
#3사분면에 속하는 경우: x- y-
elif x<0 and y<0:
    print(3)
#4사분면에 속하는 경우: x+ y-
elif x>0 and y<0:
    print(4)