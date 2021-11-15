#3) ITEmployee (наследуемся от Employee)
#1. Реализовать метод добавления одного навыка в новое свойство skills (список) новым методом add_skill
# (см. презентацию).
#2. * Реализовать метод добавления нескольких навыков в новое свойство skills (список) новым методом add_skills.
#Тут можно выбрать разные подходы: или аргумент один и он список навыков, которым вы расширяете список-свойство skill,
# или вы принимаете неопределённое количество аргументов, и все их добавляете в список-свойство skill

from lesson5.task1_2 import Employee


class ITEmployee(Employee):
    """ITEmployee description ..."""

    def __init__(self, *args, **kwargs):
        Employee.__init__(self, *args, **kwargs)
        self.skills = []

    def add_skill(self, new_skill):
        """Method add skill for ITEmployee"""
        self.skills.append(new_skill)

    def add_skills(self, *new_skills):
        """Method add skills for ITEmployee"""
        self.skills.extend(new_skills)

    def __str__(self):
        return f"ITEmployee {self.skills}"


if __name__ == "__main__":
    i = ITEmployee("Test User", 1992, position="QA", experience=7, salary=2000)
    i.add_skill("Python")
    i.add_skill("QA")
    i.add_skills("test", "dev")
    #print(i.skills)
    print(i)
