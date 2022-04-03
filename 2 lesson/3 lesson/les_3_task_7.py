# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

if array[0] < array[1]:
    min_1 = 0
    min_2 = 1
else:
    min_1 = 1
    min_2 = 0

for i in range(2, len(array)):
    if array[i] < array[min_1]:
        num = min_1
        min_1 = i
        if array[num] < array[min_2]:
            min_2 = num
    elif array[i] < array[min_2]:
        min_2 = i

if array[min_1] == array[min_2]:
    print(f'Наименьшее число {array[min_1]} повторяется в позициях {min_1} и {min_2}')
else:
    print(f'Первое наименьшее число {array[min_1]} в позиции {min_1}')
    print(f'Второе наименьшее число {array[min_2]} в позиции {min_2}')
