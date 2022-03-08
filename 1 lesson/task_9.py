# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)

# https://drive.google.com/file/d/1cSS-cYgibDqYzu0XnpoEMRdy79_oSXnL/view?usp=sharing

print('Введите три разных целых числа: ')
num_1 = float(input('1-е: '))
num_2 = float(input('2-е: '))
num_3 = float(input('3-е: '))

if num_2 < num_1 < num_3 or num_3 < num_1 < num_2:
    print('Среднее:', num_1)
elif num_1 < num_2 < num_3 or num_3 < num_2 < num_1:
    print('Среднее:', num_2)
else:
    print('Среднее:', num_3)
