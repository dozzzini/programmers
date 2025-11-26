def solution(babbling):
    answer = 0
    ok = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        new = word
        
        # 말할 수 있는 단어를 숫자로 바꾸기
        new = new.replace("aya", "1")
        new = new.replace("ye", "2")
        new = new.replace("woo", "3")
        new = new.replace("ma", "4")

        # 숫자 말고 다른 글자가 있으면 실패
        if not new.isdigit():
            continue

        # 연속된 숫자가 나오면 실패 (같은 말 연속 x)
        if "11" in new or "22" in new or "33" in new or "44" in new:
            continue

        # 여기까지 오면 성공!
        answer += 1

    return answer
