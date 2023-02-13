# Домашнее задание к Семинару №4
# Задача №1: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = (int(input('Enter number of elements of 1st set: ')))
list_1=[]
for i in range(n):
    num = int(input('Enter num: '))
    list_1.append(num)
print(set(list_1))

m = (int(input('Enter number of elements of 2d set: ')))
list_2 = []
for i in range(m):
    num = int(input('Enter num: '))
    list_2.append(num)
print(set(list_2))

k = set(list_1).intersection(set(list_2))

print(sorted(k))