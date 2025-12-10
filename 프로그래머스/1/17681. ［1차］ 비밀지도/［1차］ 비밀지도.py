def solution(n, arr1, arr2):

    answer = []    
    # 지도 1
    for i in range(n):
        number1 = arr1[i]   # arr1의 i번째 10진수 숫자
        map1_row = ""       # 이진수 문자열 결과를 저장할 변수
        
        # 이진수로 변환
        if number1 == 0:
            map1_row = "0"
        else:
            temp_num1 = number1
            # print('temp_num1:', temp_num1)
            while temp_num1 > 0:    # 몫이 0이 될 때까지 계속 나눠줄 것
                    remainder = temp_num1 % 2  # 2로 나눈 나머지 (0 또는 1)
                    # print('나머지:', remainder)
                    map1_row = str(remainder) + map1_row # 나머지를 문자열 앞쪽에 붙여 역순으로 만듦
                    # print('map1_row:',map1_row)
                    temp_num1 = temp_num1 // 2 # 몫을 다음 반복의 숫자로 사용
                    # print('temp_num1:',temp_num1)

            # 길이를 n으로 맞추기 (앞에 0 채우기)
            while len(map1_row) < n:
                map1_row = "0" + map1_row

        # 지도2
        number2 = arr2[i]
        map2_row = ""

        if number2 == 0:
            map2_row = "0"
        else:
            temp_num2 = number2
            while temp_num2 > 0:
                remainder = temp_num2 % 2  
                map2_row = str(remainder) + map2_row 
                temp_num2 = temp_num2 // 2 

        while len(map2_row) < n:
            map2_row = "0" + map2_row

        # 최종 지도
        final_row = ""

        for j in range(n):
            # j번째 칸 비교: 둘 중 하나라도 '1'(벽)이면 벽('#'), 둘 다 '0'이면 공백(' ')
            if map1_row[j] == '1' or map2_row[j] == '1':
                final_row += "#"
            else:   # 둘 다 0이어야 최종 결과에 공백 추가
                final_row += " "

        answer.append(final_row)

    return answer