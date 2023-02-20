# Домашнее задание к Семинару №6
# Задача №30: Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a = int(input('Enter the first element: '))
d = int(input('Enter step number: '))
n = int(input('Enter the number of elements: '))
arithmprogr_list = [a+i*d for i in range(n)]
print(arithmprogr_list)