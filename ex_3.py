
def spaces(string:str):
    index = 0
    try:
        while string[index] in ' ':
            index += 1
        new_string = ''
        for i in range(index,len(string)):
            new_string += string[i]
        return new_string
    except:
        return ''
while True:
    try:
        string = input('Введите строку ->')
        if len(spaces(string))==0:
            raise ValueError
        break
    except ValueError:
        print('Введена пустая стока')

dict_ = {x:string.count(x) for x in string}
for s in dict_:
    print(f'Символ "{s}" встречается в строке - {dict_[s]}')
