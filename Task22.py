#  Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12


import random

lst1 = [random.randint(-10, 10) for _ in range(int(input("Enter list 1 length: ")))]
lst2 = [random.randint(-10, 10) for _ in range(int(input("Enter list 2 length: ")))]

lst1_set = set(lst1)
lst2_set = set(lst2)
lst3_set = lst1_set.intersection(lst2_set)
lst3 = list(lst3_set)

print(lst1)
print(lst2)

print(sorted(lst3))


