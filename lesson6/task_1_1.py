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

import requests


class Books:

    def __init__(self):
        self.base_url = "http://pulse-rest-testing.herokuapp.com/"

    def create(self, book):
        resp = requests.post(self.base_url + 'books/', data=book)
        return resp.json()

    def get(self, id):
        resp = requests.get(self.base_url + 'books/' + id)
        return resp.json()

    def get_list(self):
        resp = requests.get(self.base_url + 'books')
        return resp.json()

    def update(self, id, book):
        resp = requests.put(self.base_url + 'books/' + id, data=book)
        return resp.json()

    def delete(self, id):
        resp = requests.delete(self.base_url + 'books/' + id)
        return resp.status_code == 204


def compare_book(expected, actual):
    for item in expected:
        assert item in actual
        assert expected[item] == actual[item]


books = Books()

book_dict = {
    "title": "python for qa",
    "author": "skilled qa"
}

book = books.create(book_dict)
print(book)

stored_book = books.get(str(book["id"]))
print(stored_book)
assert "id" in stored_book
compare_book(book_dict, stored_book)

stored_books = books.get_list()
print(stored_books)

for item in stored_books:
    if item["id"] == book["id"]:
        compare_book(book_dict, item)
        break

update_book_dict = {
    "author": "DEV"
}

updated_book = books.update(str(book["id"]), update_book_dict)
print(updated_book)

stored_book = books.get(str(book["id"]))
print(stored_book)

assert "id" in stored_book
compare_book(update_book_dict, stored_book)

stored_books = books.get_list()
print(stored_books)

for item in stored_books:
    if item["id"] == book["id"]:
        compare_book(update_book_dict, item)
        break

result = books.delete(str(book["id"]))
print(result)
