#Напишите программу, которая по заданному номеру четверти, 
#показывает диапазон возможных координат точек в этой четверти (x и y).
print('Hello! What is your name:')
name = str(input())
print('Hello! I am glad to see you - ', name)
print('Input number of quarter,please:')
n = int(input())
if(n < 1 or n > 4):
    print(name, 'you are broke me!')
if(n == 1):
    print('Point of this quarter is x>0 and y>0')
if(n == 2):
    print('Point of this quarter is x<0 and y>0')  
if(n == 3):
    print('Point of this quarter is x<0 and y<0')
if(n == 4):
    print('Point of this quarter is x>0 and y<0')  
