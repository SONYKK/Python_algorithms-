# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и
# 2 нечетные (3 и 5).

# https://drive.google.com/file/d/1dvpRglsYi39lXu_zsM99tuDHLtwzhPoY/view?usp=sharing

num = int(input('Введите натуральное число: '))
i_nch = 0
i_ch = 0

def chek_digit(digit):
    global i_nch
    global i_ch

    if (digit == 2) or (digit == 4) or (digit == 6) or (digit == 8) or (digit == 0):
        i_ch += 1
    else:
        i_nch += 1


if num // 10 != 0:
    while num // 10 != 0:
        digit = num % 10
        num = num // 10
        chek_digit(digit)
    chek_digit(num)
    print(f'Чётных цифр: {i_ch}, Нечётных цифр: {i_nch}')
else:
    chek_digit(num)
    print(f'Чётных цифр: {i_ch}, Нечётных цифр: {i_nch}')
