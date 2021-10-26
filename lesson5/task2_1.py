#Задание 2 (на создание новых классов)
#Создать классы
#1) Прямоугольная площадка (пример: комната) (свойства: две стороны).
#Методы:
#1.	вычисляем площадь,
#2.	вычисляем периметр.


class Room:
    """Room description ..."""

    def __init__(self, first_side, second_side):
        self.first_side = first_side
        self.second_side = second_side

    def area(self):
        """Method returns room area """
        return self.first_side * self.second_side

    def perimeter(self):
        """Method returns room perimeter """
        return (self.first_side + self.second_side)*2

    def __str__(self):
        return f"Room object {self.first_side} {self.second_side}"

r = Room(5, 5)
#print(r)
print(r.area())
print(r.perimeter())

