#Задание 2
#Создаём наборы CRUD (create, read, update, delete) тестов (как позитивные, так и негативные)
#для тестирования нашего REST API. Проверяем статус код и тело ответа.
#Не забываем про негативные тесты! Примеры: создание персонажа на книгу, которой нет,
#неправильный набор свойств книг и персонажа, не правильный тип данных.

import unittest
import requests


class BookTests(unittest.TestCase):
    def create_book(self, data):
        response = requests.post(self.base_url + "books/", data=data)
        self.assertEqual(response.status_code, 201)
        return response.json()

    def setUp(self):
        self.base_url = "http://pulse-rest-testing.herokuapp.com/"
        self.book = {"title": "1234", "author": "I"}

    def test_book_create(self):
        book = self.create_book(self.book)
        self.book["id"] = book["id"]
        self.assertDictEqual(self.book, book)

    def test_book_without_title(self):
        invalid_book = {"author": "I"}
        response = requests.post(self.base_url + "books/", data=invalid_book)
        self.assertEqual(response.status_code, 400)

    def test_get_book(self):
        book = self.create_book(self.book)
        self.book["id"] = book["id"]
        response = requests.get(self.base_url + "books/" + str(self.book["id"]))
        self.assertEqual(response .status_code, 200)
        self.assertDictEqual(self.book, book)

    def test_get_non_existent_book(self):
        response = requests.get(self.base_url + "books/" + "test")
        self.assertEqual(response .status_code, 404)

    def test_update_book(self):
        book = self.create_book(self.book)
        self.book["id"] = book["id"]
        self.updated_book = {"author": "dev"}
        response = requests.put(self.base_url + "books/" + str(self.book["id"]), data=self.updated_book)
        self.assertEqual(response .status_code, 200)
        resp_dict = response.json()
        author = resp_dict["author"]
        self.assertEqual(author, "dev")

    def test_delete_book(self):
        book = self.create_book(self.book)
        response = requests.delete(self.base_url + "books/" + str(book["id"]))
        self.assertEqual(response .status_code, 204)

    def tearDown(self):
        if "id" in self.book:
            requests.delete('{}books/{}/'.format(self.base_url, self.book["id"]))
