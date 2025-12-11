def solution(s):
    answer = True
    stack = []  # '(' 와 ')'를 임시적으로 담을 공간

    for char in s:  # char은 '('또는 ')'
        if char == '(' :
            stack.append(char)
        else :  # 닫는 기호인 경우
            # '(' 가 이미 스택 안에 있다면 닫는 기호랑 짝지어주기 위해 스택에서 빼옴
            if '(' in stack :
                stack.pop()
            # 만약 첫 번째에 나오면 그냥 false 반환
            else:
                return False
    # stack 에 여는 괄호 다 뺐다면 짝이 지어진 것
    return len(stack) == 0
