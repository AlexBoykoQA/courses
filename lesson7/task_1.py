
# Задание 1 (на создание тестов c помощью unittest)
# Создайте пару позитивных и пару негативных тестов на написанные функции из прошлого домашнего задания:
# •	функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
# •	Функцию принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами.
# Если треугольник существует, вернёт True, иначе False.
# •	Функцию принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами
# и если существует, то возвращает тип треугольника Equilateral triangle (равносторонний),
# Isosceles triangle (равнобедренный), Versatile triangle (разносторонний) или не треугольник (Not a triangle).
# •	класс ITEmployee

import unittest
from lesson3.task9 import *
from lesson4.task2 import triangle_type
from lesson5.task1_3 import ITEmployee


class LeapYear(unittest.TestCase):
    def test_leap_year(self):
        year = is_year_leap(2020)
        self.assertEqual(year, True)

    def test_not_leap_year(self):
        year = is_year_leap(2021)
        self.assertEqual(year, False)


class Triangle(unittest.TestCase):
    def test_triangle_exist(self):
        result = triangle(2, 3, 2)
        self.assertEqual(result, True)

    def test_triangle_not_exist(self):
        result = triangle(2, 3, 6)
        self.assertEqual(result, False)


class TriangleType(unittest.TestCase):
    def test_triangle_type_equilateral(self):
        result = triangle_type(3, 3, 3)
        self.assertEqual(result, "Equilateral triangle")

    def test_triangle_type_isosceles(self):
        result = triangle_type(3, 4, 4)
        self.assertEqual(result, "Isosceles triangle")

    def test_triangle_type_versatile(self):
        result = triangle_type(3, 2, 4)
        self.assertEqual(result, "Versatile triangle")

    def test_not_triangle(self):
        result = triangle_type(0, 1, 1)
        self.assertEqual(result, "Not a triangle")


class ITEmployeeTests(unittest.TestCase):
    def setUp(self):
        self.emp = ITEmployee("ALex Boyko", position='QA engineer', experience=3)

    def test_name(self):
        self.assertEqual(self.emp.name(), "ALex")
        self.assertEqual(self.emp.surname(), "Boyko")

    def test_no_skills(self):
        self.assertEqual(len(self.emp.skills), 0)

    def test_position(self):
        self.assertEqual(self.emp.get_position(), 'Middle QA engineer')

    def test_add_one_skill(self):
        self.emp.add_skill('git')
        self.assertIn('git', self.emp.skills)


if __name__ == "__main__":
    unittest.main()
