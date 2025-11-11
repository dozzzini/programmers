def solution(before, after):
    answer = 0
    # 순서 바꾸기 
    # sorted() 내장함수 => 정렬된 원소들을 새로운 객체에 담아서 반환 
    if sorted(before) == sorted(after):
        answer = 1
    else : 
        answer = 0
    
    # 순서 바꿔서 가능하면 result = 1
    # 순서 바꿔서 불가능하면 result = 0
    return answer