# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.

# Ввод:
# 6
# Вывод
# 1 2 4
# Ввод
# 24
# Вывод
# 1 2 4 8 16

n = int(input("Введите число: "))

check = 0
while (2 ** check <= n):
    print(2 ** check, end=" ")
    check += 1