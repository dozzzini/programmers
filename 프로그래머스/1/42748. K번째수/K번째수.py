def solution(array, commands):
    answer = []
    
    for command in commands:
        # print('command:', command)
        i,j,k = command[0],command[1],command[2]
        # print('i,j,k:', i, j, k)
        # i부터 j까지 자른 후에 정렬 - k 번째 숫자
        new_array = array[i-1 : j]
        new_array.sort()
        # print(new_array)
        answer.append(new_array[k-1])

    return answer