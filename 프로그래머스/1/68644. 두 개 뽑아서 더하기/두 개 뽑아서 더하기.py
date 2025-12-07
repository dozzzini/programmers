def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            plus = numbers[i] + numbers[j] 
            if plus not in answer : # 만들어 놓은 빈 배열에 두 개의 합이 없는 경우
                answer.append(plus)
            answer.sort()
    return answer