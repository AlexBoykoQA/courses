#Третий скрипт:
#•	Поэкспериментируйте создавать книги и роли с неправильными данными. Посмотрите тело и статус код ответов.
#•	Попробуйте создать роль с ссылкой на книгу, которой нет. Посмотрите тело и статус код response.


import requests
base_url = "http://pulse-rest-testing.herokuapp.com/"


def create_book(book):
    resp = requests.post(base_url + 'books/', data=book)
    #print(resp.status_code)
    #print(resp.text)
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
        print(resp.status_code)
        print(resp.content)
        return resp.json()


roles = Roles()

# create role
role_dict = {
    "name": "Tester",
    "type": "Super skill",
    "level": 80,
    "book": 100500
}
role = roles.create(role_dict)
print(role)
