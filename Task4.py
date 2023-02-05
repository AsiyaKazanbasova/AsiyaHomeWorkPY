# Домашнее задание к Семинару №1
# Задача 4: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Enter n size of choсolate: '))
m = int(input('Enter m size of choсolate: '))
k = int(input('Enter k number of pieces of choсolate: '))

if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('yes')
else:
    print('no')