# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print('Hello! What is your name:')
name = str(input())
print('Hello! I am glad to see you - ', name)
print('Input point by "X" please: ')
x = int(input())
print('Input point by "Y" please: ')
y = int(input())
if(x > 0 and y > 0):
    print('This is the first quarter of the circle!')
if(x < 0 and y > 0):
    print('This is the second quarter of the circle!')
if(x < 0 and y < 0):
    print('This is the third quarter of the circle!')
if(x > 0 and y < 0):
    print('This is the fourth quarter of the circle!')