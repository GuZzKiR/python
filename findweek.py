#Программa, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет
print('Hello! What is your name:')
name = str(input())
print('Hello! I am glad to see you - ', name)
print('Please! Input num from 1 to 7:')
a = int(input())
if (a == 6 or a == 7):
    print('Oh my God!' , name, ' , Dobby is free!')
elif (a > 7 or a == 0):
    print(name, 'you are broke me!')
elif(a == 1,2,3,4,56):
    print('I am sorry, ', name, ' , but it is time to work!')

    