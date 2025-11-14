# 가장 긴 변의 길이 a
# 나머지 두 변 b,c 
# a < b+c 
# 두 변의 길이가 담긴 배열 [num1,num2] (num1과 num2는 a,b,c 중에 2개)
# sides 중 가장 긴변이 있을 수도 있고 없을 수도 있고

def solution(sides):
    a, b = sides
    return (a + b - 1) - abs(a - b)
