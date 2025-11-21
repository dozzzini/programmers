N = int(input())
d= 2 #2부터 시작해서 나눠주기 

while N != 1 :
    if N % d != 0:
        d += 1
    else :
        N //= d
        print(d)