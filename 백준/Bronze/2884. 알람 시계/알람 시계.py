H, M = map(int, input().split())

#M이 45보다 크거나 같은 경우: H, M-45
if M >= 45:
    print(H, M-45)
# H가 0일 경우: H = 23
else:
    if H == 0:
        print(23, M+15)
#M이 45보다 작은 경우: H-1,M+15
    else:
        print(H-1, M+15)
