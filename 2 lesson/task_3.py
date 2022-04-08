# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр
# и вывести на экран. Например, если введено число 3486, надо вывести 6843.

# https://drive.google.com/file/d/1dvpRglsYi39lXu_zsM99tuDHLtwzhPoY/view?usp=sharing

num = int(input('Введите число: '))
ost = num // 10
new = num % 10

while ost != 0:
    new = new * 10 + ost % 10
    ost = ost // 10
else:
    print(new)
