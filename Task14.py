# Домашнее задание к Семинару №5
# Задача №2: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# 2 2
# 4

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

def sum(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b
    return sum(a+1, b-1)

print('The sum of two non-negative integers is:', sum(a, b))