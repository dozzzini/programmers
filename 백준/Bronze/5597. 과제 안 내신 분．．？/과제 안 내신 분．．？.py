# 체크 배열을 만들어서 숫자가 있는 경우 1, 없는 경우 0 으로 표시
check = [0] * 31 
for n in range(28):
    n = int(input())
    check[n] = 1

# 최종 정답을 넣을 answer list 만들고 여기에는 1부터 31 이내에 있는 진짜 숫자를 추가해줌
answer = []
for i in range(1,31):
    if check[i] == 0 :
        answer.append(i)
    
print(answer[0])
print(answer[1])