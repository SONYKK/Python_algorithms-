#  Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
#  Вывести на экран это число и сумму его цифр.

# https://drive.google.com/file/d/1dvpRglsYi39lXu_zsM99tuDHLtwzhPoY/view?usp=sharing

sum_1 = 0
sum_2 = 0
new = 0
old = 0


def funk1():
    global sum_1
    global new
    global sum_2
    global old
    num_1 = int(input('Введите число: '))
    if num_1 == 0:
        msg = f'Максималье число: {new}, Максимальная сумма: {sum_2}'
        print(msg)
        return msg

    old = num_1
    while num_1 != 0:
        dig_1 = num_1 % 10
        sum_1 += dig_1
        num_1 = num_1 // 10
        sum_2 = 0


def funk2():
    global sum_1
    global new
    global sum_2
    global old
    num_2 = int(input('Введите число: '))
    if num_2 == 0:
        msg = f'Максималье число: {old}, Максимальная сумма: {sum_1}'
        print(msg)
        return msg

    new = num_2
    while num_2 != 0:
        dig_2 = num_2 % 10
        sum_2 += dig_2
        num_2 = num_2 // 10
        sum_1 = 0


def funk():
    while True:
        funk1()
        if sum_2 < sum_1:
            funk2()
        if sum_2 > sum_1:
            funk1()


print(funk())
