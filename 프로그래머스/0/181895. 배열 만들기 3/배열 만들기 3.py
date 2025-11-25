def solution(arr, intervals):
    answer = []
    interval1 = intervals[0]
    interval2 = intervals[1]

    part1 = []
    for i in range(len(arr)) :
        if interval1[0] <= i <= interval1[1] :
            part1.append(arr[i])

    part2 = []
    for i in range(len(arr)) :
        if interval2[0] <= i <= interval2[1] :
            part2.append(arr[i])
    
    answer = part1 + part2

    return answer