
#2) Employee (наследуемся от Person) (добавляются свойства: должность, опыт работы, зарплата)
#* (дополнительное) Можете в конструкторе проверить, что в опыт работы и зарплата не отрицательные 😊
#Реализовать новые методы:
#1.	возвращает должность с приставкой, которая зависит от опыта работы: Junior — менее 3 лет,
# Middle — от 3 до 6 лет, Senior — больше 6 лет.
#Т.е. метод должен вернуть позицию с приставкой Junior/Middle/Senior <position>.
# Если, например, у вас объект имел должность “programmer” с опытом 2 года, метод должен вернуть “Junior programmer”
#2.	метод, который увеличивает зарплату на сумму, которую вы передаёте аргументом.


from lesson5.task1_1 import Person


class Employee(Person):
    """Employee description ..."""

    def __init__(self, full_name="", year=None, position="", experience=0, salary=0):
        if experience < 0:
            raise Exception("Invalid Experience")

        if salary < 0:
            raise Exception("Invalid Salary")

        self.full_name = full_name
        self.year = year
        self.position = position
        self.experience = experience
        self.salary = salary

    def get_position(self):
        """Method returns position according to work experience"""
        if self.experience < 3:
            return f"Junior {self.position}"

        elif self.experience < 6:
            return f"Middle {self.position}"

        return f"Senior {self.position}"

    def salary_up(self, salary):
        """Method up salary"""
        self.salary += salary

    def __str__(self):
        return f"Employee object {self.position} {self.salary}"


e = Employee("Test User", 1992, position="QA", experience=7, salary=2000)
print(e.salary_up(1500))
print(e.salary)
print(e)
