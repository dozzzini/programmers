def solution(numbers, direction):
    
    if direction == 'right':
        answer = numbers[-1:] + numbers[:-1]    # -1번째 인덱스 + -1번째 인덱스 전(포함x)까지
    else:
        answer = numbers[1:] + numbers[:1]      # 1번쨰 인덱스 + 1번째 인덱스 전(포함x)까지
    return answer