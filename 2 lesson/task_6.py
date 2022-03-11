# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться,
# больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести правильный ответ.

# https://drive.google.com/file/d/1dvpRglsYi39lXu_zsM99tuDHLtwzhPoY/view?usp=sharing

import random

my_num = random.randint(0, 100)
i = 0

def find_num(my_num):
    global i

    num = int(input(f'Угадайте случайное число от 1 до 100 (использовано {i} из 10 попыток): '))
    if num == my_num:
        return 'Ты молодец, угадал!'
    while num != my_num and i < 9:
        if num < my_num:
            i += 1
            print('Твоё число меньше моего. Попробуй ещё раз!')
            return find_num(my_num)
        else:
            i += 1
            print('Твоё число больше моего. Попробуй ещё раз!')
            return find_num(my_num)
    return f'Ты не молодец! Моё число было {my_num}'


print(find_num(my_num))
