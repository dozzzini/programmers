def solution(binomial):
    parts = binomial.split()
    a = int(parts[0])
    op = parts[1]
    b = int(parts[2])
    if op == "+":
        answer = a + b
    elif op == "-":
        answer = a - b
    elif op == "*":
        answer = a * b
    return answer