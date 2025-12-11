def solution(A,B):
    answer = 0
    # 둘이 곱해서 누적값이 최소가 되려면 한쪽은 작은 거 한쪽은 큰 걸로 매칭해야 함
    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer