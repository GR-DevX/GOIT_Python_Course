def findLetter(st:str,letter:str)->str|None:
    counter=1
    for l in st:
        if l == letter:
            return counter
        counter+=1
    return None

print(findLetter('hello','l'))
print(findLetter('hello','h'))
print(findLetter('hello','q'))

if findLetter('hello','h')is not None:
    print('found')
else:
    print('not found')