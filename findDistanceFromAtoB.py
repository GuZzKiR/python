# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


print('Hello! What is your name:')
name = str(input())
print('Hello! I am glad to see you - ', name)
print('Input coordinates first line x1 and x2, please:')
x1 = float(input())
x2 = float(input())
print('Input coordinates second line y1 and y2, please:')
y1 = float(input())
y2 = float(input())
distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (0.5)

print(distance)