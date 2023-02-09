# Домашнее задание к Семинару №3
# Задача №1: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример:
# 5
# 1 2 3 4 5
# 3
# -> 1
n = int(input('Enter a number for N: '))
num_list = []

for i in range(n):
    num = int(input('Enter a number for Ai: '))
    num_list.append(num)

x = int(input('Enter a number for X: '))
count = 0
for x in num_list:
    if x == num:
        count += 1
print('Number X occurs in array A', count, end = ' time(-s)')