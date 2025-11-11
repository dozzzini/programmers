def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list),n) : # 0부터 num_list길이까지 n씩 건너뛰면서 개수 담음
        answer.append(num_list[i:i+n])
    return answer

# 만약 n이 2면 range(0, 8, 2)
# num_list[0:2]
# num_list[2:4] 이런 식 