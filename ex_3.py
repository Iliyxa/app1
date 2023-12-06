
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
a = { x: string.count(x) for x in string if x not in " 0123456789"}
print(a)
for k,v in a.items():
    print(f'Символ "{k}" встречается в строке - {v} раз')

