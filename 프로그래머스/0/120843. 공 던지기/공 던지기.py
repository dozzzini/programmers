# 두 칸씩 점프
# result 는 numbers 안의 값일 수밖에 없음 -> numbers[] 으로 놓고 [] 안에 뭐가 들어갈지 생각
# 총 이동칸수 = 2 * 이동한 횟수 (2*(k-1))
# 배열 길이 넘으면 앞으로 돌아가기

def solution(numbers, k):
    return numbers[2 * (k-1) % len(numbers)]
    
