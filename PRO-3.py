word = 'pythonisttttttttttt'
dict_ = {x:word.count(x) for x in word}
print(dict_)
for key, value in dict_.items():
    print(f'Символ {key} встречается в строке - {value}')