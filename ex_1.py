
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
matrix = [[] for _ in range(n)]
summa_all = []

for i in range(n):
    summa = 0
    for j in range(m):
        matrix[i].append(j+1+i+1)
        summa += i+j+2
    summa_all.append(summa)
        
for line in matrix:
        for element in line:
            print(element, end=' ')
        print()

for i in range(n):
    print(f'Сумма {i+1} - {summa_all[i]}', end=' ')
