
"""
Задание 6
Даны три целых числа. Определите, сколько среди них совпадающих.
Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа
"""

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)
