#Тестовое приложение с REST API: http://pulse-rest-testing.herokuapp.com/
#Создаём один скрипт:
#•	Создаём книгу POST /books/, вы запоминаете его id.
#•	Проверяете, что она создалась и доступна по ссылке GET/books/[id]
#•	Проверяете, что она есть в списке книг по запросу GET /books/
#•	Изменяете данные этой книги методом PUT /books/[id]/
#•	Проверяете, что она изменилась и доступна по ссылке /books/[id]
#•	Проверяете, что она есть в списке книг по GET /books/ с новыми данными.
#•	Удаляете эту книгу методом DELETE /books/[id].
#Все проверки делать программно, а не глазами, т.е. проверить,
# что в теле response данные такие же как в вашем исходном словаре путём сравнения значений в словарях
#Второй скрипт:
#тоже самое с ролями. Здесь немного поинтересней, т.к. есть связка с книгой, которая уже должна существовать.
# Создайте книгу заранее в этом же скрипте, не надейтесь на книги, которые вы видите, их кто-то другой может удалить.

import requests
base_url = "http://pulse-rest-testing.herokuapp.com/"


def create_book(book):
    resp = requests.post(base_url + 'books/', data=book)
    return resp.json()


book_dict = {
    "title": "Business",
    "author": "Unknown"
}


book = create_book(book_dict)
# print(book)
book_id = book["id"]
# print(book_id)


class Roles:

    def __init__(self):
        self.base_url = "http://pulse-rest-testing.herokuapp.com/"

    def create(self, role):
        resp = requests.post(self.base_url + 'roles/', data=role)
        return resp.json()

    def get(self, id):
        resp = requests.get(self.base_url + 'roles/' + id)
        return resp.json()

    def get_list(self):
        resp = requests.get(self.base_url + 'roles/')
        return resp.json()

    def update(self, id, role):
        resp = requests.put(self.base_url + 'roles/' + id, data=role)
        return resp.json()

    def delete(self, id):
        resp = requests.delete(self.base_url + 'roles/' + id)
        return resp.status_code == 204


def compare_role(expected, actual):
    for item in expected:
        assert item in actual
        assert expected[item] == actual[item]


roles = Roles()

# create role
role_dict = {
    "name": "Tester",
    "type": "Super skill",
    "level": 80,
    "book": book_id
}
role = roles.create(role_dict)
#print(role)

# get role
stored_role = roles.get(str(role["id"]))
# print(stored_role)
assert "id" in stored_role
compare_role(role_dict, stored_role)

# get roles
stored_roles = roles.get_list()
# print(stored_roles)
for item in stored_roles:
    if item["id"] == role["id"]:
        compare_role(role_dict, item)
        break

# update role
update_role_dict = {
    "level": 79
}
updated_role = roles.update(str(role["id"]), update_role_dict)
# print(updated_role)

result = roles.delete(str(role["id"]))
print(result)
