# По введенным пользователем длинам трех отрезков определить,
# можно ли составить из этих отрезков треугольник.
# Если да, определить, будет ли треугольник разносторонним, равнобедренным или равносторонним.

# https://drive.google.com/file/d/1cSS-cYgibDqYzu0XnpoEMRdy79_oSXnL/view?usp=sharing

line_1 = float(input("Введите длину 1 стороны треугольника: "))
line_2 = float(input("Введите длину 2 стороны треугольника: "))
line_3 = float(input("Введите длину 3 стороны треугольника: "))

if line_1 + line_2 <= line_3 or line_1 + line_3 <= line_2 or line_2 + line_3 <= line_1:
    print("Треугольник не получится!")
elif line_1 != line_2 and line_1 != line_3 and line_2 != line_3:
    print("Треугольник разносторонний")
elif line_1 == line_2 == line_3:
    print("Треугольник равносторонний")
else:
    print("Треугольник равнобедренный")
