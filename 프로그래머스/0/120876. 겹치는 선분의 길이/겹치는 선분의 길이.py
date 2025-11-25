def solution(lines):
    answer = 0
    
    # 첫 번째 구간 내에 있는 숫자들
    num1_list = []
    for i in range(lines[0][0], lines[0][1]) :
         num1_list.append(i)
    
    # 두 번째 구간 내에 있는 숫자들
    num2_list = []
    for j in range(lines[1][0], lines[1][1]) :
        num2_list.append(j)
    
    # 세 번째 구간 내에 있는 숫자들
    num3_list = []
    for k in range(lines[2][0], lines[2][1]) :
        num3_list.append(k)

    nums = num1_list + num2_list + num3_list
    print(nums)

    # nums 에 있는 값들 중복 제거
    unique_nums = []
    for x in nums :
        if x not in unique_nums :
            unique_nums.append(x)

    # 중복 제거된 것에서 몇 번 나왔는지 세기
    answer = 0
    for x in unique_nums :
        cnt = nums.count(x)
        print(cnt)

        if cnt >= 2:  
            answer += 1

    return answer