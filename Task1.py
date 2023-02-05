# Домашнее задание к Семинару №1
# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = int(input('Enter any three-digit number: '))

d1 = n % 10
d2 = n % 100 // 10
d3 = n // 100
 
print("The sum of digits of a number is:", d1 + d2 + d3)