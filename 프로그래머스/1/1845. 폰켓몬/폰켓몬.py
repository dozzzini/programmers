def solution(nums):
    answer = 0
    # 선택할 수 있는 최대 마리 수 (N/2)
    max_selection = len(nums) //2
    print('max_selection:',max_selection)

    # 연구실에 존재하는 폰켓몬의 실제 종류 수 -> set 사용해서 중복된 요소 제거
    unique_kinds = len(set(nums))
    print("unique_kinds:",unique_kinds)

    # 최대가 되는 것 : max_selection vs unique_kinds 중 더 작은 값
    if unique_kinds < max_selection :
        answer = unique_kinds
    else:
        answer = max_selection
    return answer