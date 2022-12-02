# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

print('Hello! What is your name:')
name = str(input())
print('Hello! I am glad to see you - ', name)
def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n-1)
print(f'{name} введите любое число! ')
n = int(input())
if n == 0:
    print(f'Хитрец {name} введите число больше 0 ')
    n = int(input())
list = []
for i in range(1, n + 1):
    list.append(mult(i))
print(f'{name} - произведение чисел от 1 до {n}: {list}')
