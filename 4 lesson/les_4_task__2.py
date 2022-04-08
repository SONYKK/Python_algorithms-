import timeit
import cProfile

"""2). Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна
принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

- Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его
улучшить/оптимизировать под задачу.

- Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту."""


HOLE = 0


def sieve_eratosfen(num):           # noqa
    size = num ** 3
    my_list = [i for i in range(size)]
    my_list[1] = HOLE
    for i in range(2, size):
        if my_list[i] != HOLE:
            j = i ** 2
            while j < size:
                my_list[j] = HOLE
                j += i

    res = [i for i in my_list if i != HOLE]
    return res[num - 1]


print(sieve_eratosfen(10))

print(timeit.timeit("sieve_eratosfen(100)", number=100, globals=globals()))         # 42.487126200000006

cProfile.run('sieve_eratosfen(100)')

"""   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.009    0.009    0.421    0.421 <string>:1(<module>)
        1    0.324    0.324    0.412    0.412 les_4_task_2.py:18(sieve_eratosfen)
        1    0.050    0.050    0.050    0.050 les_4_task_2.py:20(<listcomp>)
        1    0.037    0.037    0.037    0.037 les_4_task_2.py:29(<listcomp>)
        1    0.001    0.001    0.421    0.421 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""


def prime(n):
    i = 1
    number = 2

    while i < n:
        number += 1
        for item in range(2, number):
            if number % item == 0:
                break
            else:
                i += 1
    return number


print(prime(100))

print(timeit.timeit("prime(100)", number=100, globals=globals()))           # 0.0013333000000000927

cProfile.run('prime(100)')

"""   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_2.py:52(prime)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""