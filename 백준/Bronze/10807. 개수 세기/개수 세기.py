n = int(input())
numbers = list(map(int, input().split()))
blank = int(input())

count = numbers.count(blank)
print(count)