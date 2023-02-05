# Домашнее задание к Семинару №2
# Задача №2: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
# Пример:
# 4 4 -> 2 2
# 5 6 -> 2 3

# Решени: из условия следует, что: s = x + y -> y = s - x
s = int(input('Enter a sum of "x" and "y": '))
p = int(input('Enter a product of "x" and "y": '))

for x in range(1, 1001):
    y = s - x
    if x <= y and x * y == p:
        print(x, y)