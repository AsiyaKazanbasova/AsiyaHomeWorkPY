# Домашнее задание к Семинару №5
# Задача №1: Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def power_a_b(a, b):
    if b == 0:
        return 1
    elif (a == 1):
        return (a)
    return (a ** b)

a = int(input('Enter a number: '))
b = int(input('Enter power for "a": '))

result = power_a_b(b)
print('The result of exponentiation is:', result)