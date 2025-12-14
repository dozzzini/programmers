def solution(s):
    answer_list = [] 
    splited_s = s.split(' ')
    for letter in splited_s : 
        answer_list.append(letter.capitalize())
        answer = ' '.join(answer_list)
    
    return answer