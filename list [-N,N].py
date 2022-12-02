# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. 
# Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

print('Hello! What is your name:')
name = str(input())
print('Hello! I am glad to see you - ', name)
print(f'{name} введите любое число! ')
n = int(input())
if n == 0:
    print(f'Хитрец {name} введите число больше 0 ')
    n = int(input())
list = list(range(-n, n+1))
print(list)    
print('Введите элементы списка через пробел:')
ell = input().split()
for i in range(len(ell)):
    ell[i] = int(ell[i])
print(ell)










