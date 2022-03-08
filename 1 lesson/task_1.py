# Найти сумму и произведение цифр введённого пользователем трехзначного числа

# https://drive.google.com/file/d/1cSS-cYgibDqYzu0XnpoEMRdy79_oSXnL/view?usp=sharing

number = int(input('Введите натуральное трёхзначное число: '))

digit_1 = number // 100
digit_2 = number % 100 // 10
digit_3 = number % 10
mult = digit_1 * digit_2 * digit_3
summ = digit_1 + digit_2 + digit_3
print(f'Сумма = {summ}')
print(f'Произведение = {mult}')
