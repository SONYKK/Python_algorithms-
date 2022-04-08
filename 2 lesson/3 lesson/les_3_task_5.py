# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве. Примечание к задаче:
# пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

i = 0
num = None
for i in range(len(array)):
    if array[i] < 0 and num is None:
        num = i
    elif array[num] < array[i] < 0:
        num = i
    i += 1

if num is not None:
    print(f'Максимальный отрицательный элемент массива {array[num]}. Его индекс: {num}')
