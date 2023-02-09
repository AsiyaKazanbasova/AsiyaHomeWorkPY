# Домашнее задание к Семинару №3
# Задача №2: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример:
# 5
# 1 2 3 4 5
# 6
# -> 5
n = int(input('Enter a number for N: '))
num_list = []

for i in range(n):
    num = int(input('Enter a number for Ai: '))
    num_list.append(num)

x = int(input('Enter a number for X: '))
closeinsize = 0
for i in range(len(num_list)):
    if (x - num_list[i]) < x - closeinsize and x - num_list[i] > 0:
        closeinsize = i
print(num_list[closeinsize])