# 1+2 -2+3 => 4
# Z가 없는 경우 -> 다 더함
# 10 -10 + 20 - 20 + 1 => 1

# s는 문자열 -> 공백을 기준으로 쪼개주기 .split()

def solution(s):
    total = 0 # 지금까지 더한 값 넣을 공간
    last = 0  # 바로 전에 더한 숫자 기억할 공간
    
    for x in s.split(): # 공백 기준으로 분리
        if x == "Z":    # z이면
            total -= last   # z가 나오면 지금까지 나온 숫자에서 마지막 숫자 빼기
            last = 0        # 마지막 숫자에 대한 기억 날려버리기(빼줬으니까)
        else:               # 숫자면
            num = int(x)    # 문자를 숫자로 바꾼 후에     
            total += num    # 그냥 더해줌
            last = num      # 다 더해준 값이 마지막 숫자
            
    return total
