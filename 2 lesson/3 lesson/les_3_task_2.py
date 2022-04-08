# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями
# 0, 3, 4, 5, (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

import random

SIZE = 7
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

my_list = []
for pos, element in enumerate(array):
    if element % 2 == 0:
        my_list.append(pos)
print(f'Индексы четных элементов: {my_list}')
