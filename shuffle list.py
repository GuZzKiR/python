# Реализуйте алгоритм перемешивания списка.

from random import randint


print('Hello! What is your name:')
name = str(input())
print('Hello! I am glad to see you - ', name)
print(f'{name} введите любое число! ')
n = int(input())
if n == 0:
    print(f'Хитрец {name} введите число больше 0 ')
    n = int(input())
list= [randint(1, 9) for i in range(n)]
print(list)
list2 = sorted(list)
print(list2)