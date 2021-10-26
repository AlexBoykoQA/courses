#3) Точка на карте (свойства: X, Y).
#Методы:
#1.	Нужно вычислить расстояние до начала координат,
#2.	* вычисляется расстояние между точкой и другой точкой экземпляром этого же класса
#3.	** перевод в другие системы координат
#3) Для всех классов сделайте __str__, чтоб объекты красиво выводились на экран!


from math import sqrt


class Point:
    """A point on the map..."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        """Method returns the distance to the origin"""
        return sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return f"Point object "


p = Point(5, 5)
print(p.distance())
