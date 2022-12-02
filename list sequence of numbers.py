# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

print('Hello! What is your name:')
name = str(input())
print('Hello! I am glad to see you - ', name)
print(f'{name} введите любое число! ')
n = int(input())
if n == 0:
    print(f'Хитрец {name} введите число больше 0 ')
    n = int(input())
list = [round((1+1/i)**i, 2) for i in range(1, n+1)]
print(f'Последовательность: {list}\nСумма: {round(sum(list), 3)}')
