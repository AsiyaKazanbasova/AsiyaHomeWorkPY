# Домашнее задание к Семинару №6
# Задача №32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

n = int(input('Enter the number of elements: '))
list_1 = [int(input('Enter a number: ')) for i in range(n)]
print(list_1)
min_num = int(input('Minimum: '))
max_num = int(input('Maximum: '))
index_list = []
if max_num>=min_num:
    for i in range(len(list_1)):
        if max_num>=list_1[i] and min_num<=list_1[i]:
            index_list.append(i)
    print('Indexes of array elements between Minimum and Maximum are:', index_list)