def solution(letter):
    answer = ''
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    
    m_k = morse.keys()      # 부호만
    m_v = morse.values()    # 문자만
    
    letter_list = letter.split(' ') # 공백을 기준으로 letter 분리 
    
    for l in letter_list :
        for k in m_k : 
            if l == k:
                answer += morse[k]
    return answer