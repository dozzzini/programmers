def solution(myString):
    for ch in "abcdefghijk": 
        myString = myString.replace(ch, 'l')
    return myString
