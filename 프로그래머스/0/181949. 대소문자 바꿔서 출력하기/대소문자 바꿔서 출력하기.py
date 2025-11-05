str = input()
for i in str:
    if i.isupper() == True:
        print(i.lower(), end = '')
    if i.islower() == True:
        print(i.upper(), end = '')