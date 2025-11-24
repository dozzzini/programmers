def solution(common):
    
    # 등차수열인 경우
    if common[1] - common[0] == common[2] - common[1] :
        # 등차수열일 때 result는 차이를 common[-1] 에 더해주면 되고 
        return common[-1] + (common[1] - common[0])

    # 등비수열인 경우
    if common[0] != 0 and common[1] != 0:
        # 등비수열일 때 result는 나눠진 값? 을 common[-1]에 곱해줘야 함
        return common[-1] * (common[1] / common[0])
