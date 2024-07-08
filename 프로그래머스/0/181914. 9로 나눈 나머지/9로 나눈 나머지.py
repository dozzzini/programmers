def solution(number):
    sum = 0
    
    for num in str(number):
        sum += int(num)
    answer = sum % 9
    return answer