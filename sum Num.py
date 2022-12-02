# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

print('Hello! What is your name:')
name = str(input())
print('Hello! I am glad to see you - ', name)
def sumnum(n):
    sum = 0
    for i in str(n):
        if i!= ',':
            sum += int(i)
    return sum  
print(f'{name} введите любое число! ')
n = float(input())
if n == 0:
    print(f'Хитрец {name} введите число больше 0 ')
    n = float(input())
print(f'Сумма цифр: {sumnum(n)}')   
