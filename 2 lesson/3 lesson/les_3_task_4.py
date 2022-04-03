# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

my_dict = {}
i = 1
num = None
for element in array:
    if element in my_dict:
        my_dict[element] += 1
    if element not in my_dict:
        my_dict[element] = 1
    if i < my_dict[element]:
        i = my_dict[element]
        num = element

if num:
    print(f'Число {num} встречается чаще других (его {i})')
else:
    print('Нет повторяющихся чисел')
