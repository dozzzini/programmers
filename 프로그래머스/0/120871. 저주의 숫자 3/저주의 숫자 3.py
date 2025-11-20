# 숫자를 1부터 차례대로 볼 때
# 숫자에 3이 들어가면 제외
# 숫자가 3으로 나누어 떨어지면 제외

def solution(n):
    count = 0
    num = 1

    while True:
        # 숫자에 3이 없거나 3의 배수가 아닐 때에만 숫자 증가
        if num % 3 != 0 and '3' not in str(num):
            count += 1
            if count == n:  # 들어온 숫자랑 같으면 그만하기
                return num
        
        num += 1