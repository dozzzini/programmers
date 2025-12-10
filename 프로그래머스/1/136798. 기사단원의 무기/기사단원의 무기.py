def solution(number, limit, power):
    # 기본 공격력 = 기사 번호 K의 약수 개수

    # 만약 기본 공격력 < limit :
        # 최종 공격력 = 기본 공격력
    # 만약 기본 공격력 > limit :
        # 최종 공격력 = 대체 공격력(power)

    # 1번~number 번 기사까지의 모든 기사의 최종 공격력 계산해서 합산

#     # n의 약수 개수 계산 함수 => (이렇게 작성하면 시간 초과 오류 뜨게 됨)
#     def yaksoo_count(n) :
#         count = 0
#         for i in range(1,n+1):
#             if n % i == 0:
#                 count += 1
#         return count

    # (정리) 효율성 고려해서 n의 약수 개수 계산 함수
    def yaksoo_count(n) :
            count = 0
            # 반복 범위를 n의 제곱근까지로 줄이기
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    if i * i == n:
                        count += 1
                    else:
                        count += 2
            return count
        
    answer = 0  # 총 필요한 철의 무게
    for j in range(1, number+1) :
        basic = yaksoo_count(j)

        if basic > limit :
            final = power 
        else:
            final = basic
            
        answer += final


    return answer