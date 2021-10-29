#Переделываем (а что-то повторяем и закрепляем) наши классы таким образом:
#1) Person (два свойства: 1. теперь full_name пусть будет свойством, а не функцией (одно поле, мы ожидаем - тип строка и состоит из двух слов «имя фамилия»), а свойств name и surname нету, 2. год рождения).
#Реализовать методы, которые:
#1.	выделяет только имя из full_name
#2.	выделяет только фамилию из full_name;
#3.	вычисляет сколько лет было/есть/исполнится в году, который передаётся параметром (obj.age_in(year)); если не передавать параметр, по умолчанию, сколько лет в этом году;
#* (дополнительное) Можете в конструкторе проверить, что в full_name передаётся строка, состоящая из двух слов, если нет, вызывайте исключение 😊
#* (дополнительное) Можете в конструкторе проверить, что в год рождения меньше или равно 2020 (текущий год – для продвинутых), но больше или равно 1900. Если нет, вызывайте исключение
import datetime


class Person:
    """Person description ..."""

    def __init__(self, full_name, year):

        if len(full_name.strip().split(' ')) != 2:
            raise ValueError("Invalid fullname")

        if year > datetime.datetime.now().year or year < 1900:
            raise ValueError("Invalid year")

        self.full_name = full_name
        self.year = year

    def name(self):
        """Returns person name"""
        name = self.full_name.strip().split(' ')[0]
        return name

    def surname(self):
        """Returns person surname"""
        surname = self.full_name.strip().split(' ')[-1]
        return surname

    def age_in(self, year=datetime.datetime.now().year):
        """Returns person age in ... """
        return year - self.year

    def __str__(self):
        return f"Person object {self.full_name} {self.year}"


p = Person("Test User", 2021)
print(p)
#print(p.name())
#print(p.surname())
#print(p.age_in())
