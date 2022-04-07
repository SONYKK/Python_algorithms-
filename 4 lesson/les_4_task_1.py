import timeit
import cProfile

"""" 1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках
домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать,
для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему."""


# Урок 2, задача 4.
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

# Вариант 1
def devil_sum_1(n):
    i = 1
    sum_ = 0
    el = 1
    my_list = [el, ]

    while i != n:
        i += 1
        sum_ += el
        el = el / -2
        my_list.append(el)
    return f'Ваш ряд элементов: {my_list}, их сумма: {sum_}'


print(devil_sum_1(10))


# вариант 2
def devil_sum_2(n):
    summa_2 = 1 * (1 - (-0.5) ** n) / (1 - (-0.5))
    return summa_2


print(devil_sum_2(10))


# вариант 3
def devil_sum_3(num, start=1.0, step=-0.5):
    if num == 1:
        return start
    if num > 55:
        return 2 / 3
    return start + devil_sum_3(num - 1, start * step)


print(devil_sum_3(10))


print('Исследование первой функции')
print(timeit.timeit("devil_sum_1(10)", number=100, globals=globals()))      # 0.0005522000000000027
print(timeit.timeit("devil_sum_1(20)", number=100, globals=globals()))      # 0.0014330000000000037
print(timeit.timeit("devil_sum_1(30)", number=100, globals=globals()))      # 0.0029647000000000007
print(timeit.timeit("devil_sum_1(40)", number=100, globals=globals()))      # 0.004118700000000003
print(timeit.timeit("devil_sum_1(50)", number=100, globals=globals()))      # 0.006121799999999997
print(timeit.timeit("devil_sum_1(60)", number=100, globals=globals()))      # 0.0070553000000000005
print(timeit.timeit("devil_sum_1(70)", number=100, globals=globals()))      # 0.007308200000000001
print(timeit.timeit("devil_sum_1(80)", number=100, globals=globals()))      # 0.0091093
print(timeit.timeit("devil_sum_1(90)", number=100, globals=globals()))      # 0.01043029999999999
print(timeit.timeit("devil_sum_1(100)", number=100, globals=globals()))     # 0.012788500000000008

cProfile.run("devil_sum_1(1000000)")

"""   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.018    0.018    0.509    0.509 <string>:1(<module>)
        1    0.385    0.385    0.491    0.491 les_4_task_1.py:20(devil_sum_1)
        1    0.000    0.000    0.509    0.509 {built-in method builtins.exec}
   999999    0.106    0.000    0.106    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

print('Исследование второй функции')
print(timeit.timeit("devil_sum_2(100)", number=100, globals=globals()))      # 3.310000000000812e-05
print(timeit.timeit("devil_sum_2(200)", number=100, globals=globals()))      # 3.100000000000325e-05
print(timeit.timeit("devil_sum_2(300)", number=100, globals=globals()))      # 3.109999999995061e-05
print(timeit.timeit("devil_sum_2(400)", number=100, globals=globals()))      # 3.0799999999997496e-05
print(timeit.timeit("devil_sum_2(500)", number=100, globals=globals()))      # 3.069999999993911e-05
print(timeit.timeit("devil_sum_2(600)", number=100, globals=globals()))      # 3.0799999999997496e-05
print(timeit.timeit("devil_sum_2(700)", number=100, globals=globals()))      # 4.3299999999968364e-05
print(timeit.timeit("devil_sum_2(800)", number=100, globals=globals()))      # 3.180000000002625e-05
print(timeit.timeit("devil_sum_2(900)", number=100, globals=globals()))      # 3.090000000005588e-05
print(timeit.timeit("devil_sum_2(1000)", number=100, globals=globals()))     # 3.0599999999991745e-05


cProfile.run("devil_sum_2(9000000)")

"""   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:38(devil_sum_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

print('Исследование третьей функции')
print(timeit.timeit("devil_sum_3(1000)", number=100, globals=globals()))      # 1.289999999998237e-05
print(timeit.timeit("devil_sum_3(2000)", number=100, globals=globals()))      # 1.2400000000023503e-05
print(timeit.timeit("devil_sum_3(3000)", number=100, globals=globals()))      # 1.2299999999965117e-05
print(timeit.timeit("devil_sum_3(4000)", number=100, globals=globals()))      # 1.2299999999965117e-05
print(timeit.timeit("devil_sum_3(5000)", number=100, globals=globals()))      # 1.2400000000023503e-05
print(timeit.timeit("devil_sum_3(6000)", number=100, globals=globals()))      # 1.2200000000017752e-05
print(timeit.timeit("devil_sum_3(7000)", number=100, globals=globals()))      # 1.2200000000017752e-05
print(timeit.timeit("devil_sum_3(8000)", number=100, globals=globals()))      # 1.2300000000076139e-05
print(timeit.timeit("devil_sum_3(9000)", number=100, globals=globals()))      # 1.2299999999965117e-05
print(timeit.timeit("devil_sum_3(10000)", number=100, globals=globals()))     # 1.2300000000076139e-05


cProfile.run("devil_sum_3(9000000)")

"""   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:47(devil_sum_3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# ______________________________________________________________________________________________________________________

"""
Вывод:
    1 функция - линейная асимптотика
    2 функция - думаю, с учетом погрешностей измерения, можно говорить о константной асимптотике
    3 функция - константная, но более быстрая, т.к. выполняет гораздо меньшее количество операций, а далее возвращает константу
"""