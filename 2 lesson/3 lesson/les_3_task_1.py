#В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому
# из чисел в диапазоне от 2 до 9.

FIRST_NUM = 2
LAST_NUM = 99
DIGIT_1 = 2
DIGIT_2 = 9
i = 0

for element in range(DIGIT_1, DIGIT_2 + 1):
    for el in range(FIRST_NUM, LAST_NUM + 1):
        if el % element == 0:
            i += 1
    print(f'Целых {i} чисел кратно цифре {element}.')
    