
from random import *

class MxN_ERROR (Exception):
    pass

while True:
        try:
            m = int(input('Введите кол-во столбцов = '))
            n = int(input('Введите кол-во строк = '))
            if m < 2 or n < 2:
                    raise MxN_ERROR
            break
        except ValueError:
            print('ERROR - 0!\nВведенно не целое число')
        except MxN_ERROR:
            print('ERROR - 1!\nНе может быть меньше 2')

matrix = [[randint(0,9) for _ in range(m)] for _ in range(n)]
maximum_summa = -10**11

for i in range(n):
    summa = 0
    for j in range(m):
        summa += matrix[i][j]
        print(matrix[i][j], end=' ')
    print('')
    if summa > maximum_summa:
        maximum_summa = summa
        index = i

print('Cтрока с максимальной суммой')
for element in matrix[index]:
     print(element, end=' ')
print()
print(f'Максимальная сумма в {index+1} строке- {maximum_summa}')
