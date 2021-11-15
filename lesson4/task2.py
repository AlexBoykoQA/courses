#1)	Пишем функцию, которая попросит ввести число. Пока он не введёт правильно, просите его ввести.
# Функция возвращает введённое число.

def number_validator():
    required_number = 7
    while True:
        number = int(input("Enter number: "))
        if number == required_number:
            print("ok")
            break
    return number


if __name__ == "__main__":
    number_validator()

#2)Пишем функцию, которая попросит пользователя ввести слово (строка без пробелов в середине,
#а вначале и в конце пробелы могут быть – их стоит удалить перед проверкой).
#Пока он не введёт правильно, просите его ввести. Функция возвращает введённое слово.

def word_validator():
    required_word = "test"
    while True:
        word = input("Enter word \n")
        word = word.strip()
        if word == required_word:
            print("ok")
            break
    return word


if __name__ == "__main__":
    word_validator()

#3)	Функция принимает три числа a, b, c. Функция должна определить,
# существует ли треугольник с такими сторонами и если существует, то возвращает тип треугольника
# Equilateral triangle (равносторонний), Isosceles triangle (равнобедренный),
# Versatile triangle (разносторонний) или не треугольник (Not a triangle).


def triangle_type(a, b, c):

    if (a + b > c) and (a + c > b) and (b + c > a):

        if a == b and b == c:
            return 'Equilateral triangle'

        elif a == b or b == c or a == c:
            return 'Isosceles triangle'

        else:
            return 'Versatile triangle'

    else:
        return 'Not a triangle'


if __name__ == "__main__":
    print(triangle_type(4, 4, 4))

#4 Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2),
# вычисляющую расстояние между точками с координатами (x1, y1) и (x2, y2).
# Считайте четыре действительных числа от пользователя и выведите результат работы этой функции.

from math import sqrt
def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)


if __name__ == "__main__":
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))

    print(distance(x1, y1, x2, y2))

#5 Напишите функцию, которая удаляет все небуквенные символы внутри строки (ограничимся латинским алфавитом).



def symbols_filter(s):
    s1 = "".join(c for c in s if c.isalpha())
    return s1


if __name__ == "__main__":
    s = "Hello$@ Python3&12"
    print(symbols_filter(s))

