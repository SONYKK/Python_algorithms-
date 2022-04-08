# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

# https://drive.google.com/file/d/1cSS-cYgibDqYzu0XnpoEMRdy79_oSXnL/view?usp=sharing

num = int(input('Номер буквы английского алфавита (1-26): '))
num = ord('a') + num - 1
print(f'Это буква {chr(num)}')
