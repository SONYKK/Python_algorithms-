# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

# https://drive.google.com/file/d/1dvpRglsYi39lXu_zsM99tuDHLtwzhPoY/view?usp=sharing

n = int(input('Введите количество элементов: '))
i = 1
sum = 1     # noqa
el = 1


def funk(n):
    global i
    global sum      # noqa
    global el
    el = el / -2

    if i != n:
        i += 1
        sum += el
        return funk(n)
    else:
        return sum


print(funk(n))
