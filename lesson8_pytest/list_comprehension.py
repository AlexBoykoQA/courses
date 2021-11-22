# 1)Создайте список 2 в степени N, где N от 0 до 20.
# 2)У вас есть список целых чисел. Создайте новый список остатков от деления на 3 чисел из исходного списка.
# 3)У вас есть список, в котором могут быть разные типы данных. Создайте новый список только чисел из этого списка.
# 4)У вас есть список, в котором могут быть разные типы данных.
# Создайте новый список только строк, при этом удалите усе небуквенные символы из них.
# Воспользуйтесь функцией из предыдущего задания (импортируйте её из другого своего файла)
# 5)У вас есть словарь – характеристик человека.
# Ключи, например,: “name”, “surname”, “age”, “position”, “address”, “skills”.
# -Сгенерируйте новый словарь с такими же ключами, а в значениях типы значений.
# -Сгенерируйте новый словарь с только парами ключ-значение, если значение исходного словаря было строкой.
# Значения нового словаря должны быть переведены в нижний регистр и удалены всё небуквенные символы из них.


# 1
nums = [2**i for i in range(0, 21)]
print(nums)


# 2
new_list = [i % 3 for i in nums]
print(new_list)

# 3
dif_type_list = ["test", 2, 3]
numbers_list = [i for i in dif_type_list if type(i) is int]
print(numbers_list)

# 4
from lesson4.task2 import symbols_filter
dif_type_list = ["test", 2, 3, "qa123"]
numbers_list = [symbols_filter(i) for i in dif_type_list if type(i) is str]
print(numbers_list)

# 5
my_dict = {'name': 'Jack', 'surname': 'Varabei', 'age': 26, 'skills': ["jira", "redmine"]}

new_dict = {key: type(my_dict[key]).__name__ for key in my_dict}
print(new_dict)

new_dict = {key: symbols_filter(my_dict[key]).lower() for key in my_dict if type(my_dict[key]) is str}
print(new_dict)
