# Задание 3
# Тестируем фильтры:
# - сначала просто научитесь делать эти запросы;
# - потом тоже встраиваем в тесты.
# В нашем тестовом REST приложении уже реализованы фильтры для roles.
# Вы можете получать частичный список ролей, фильтруя по book_id, type и level, передавая их в качестве параметра.
# Запрос - дай мне роли из книги "такой-то" книги, выглядит так:
# http://pulse-rest-testing.herokuapp.com/roles/?book_id={id}
# Запрос - дай мне роли "такого-то" типа, выглядит так:
# http://pulse-rest-testing.herokuapp.com/roles/?type={text}
# Запрос - дай мне роли "такого-то" уровня, выглядит так:
# http://pulse-rest-testing.herokuapp.com/roles/?level={number}
# Для уровня level сделано ещё кое-что поинтереснее 
# может присутствовать не только параметр level=, а и
# level__lt={number} - уровень level меньше, чем number
# level__lte={number} - уровень level меньше или равно, чем number
# level__gt={number} - уровень level больше, чем number
# level__gte={number} - уровень level больше или равно, чем number
# Эти все фильтры можно объединять. Пример:
# http://pulse-rest-testing.herokuapp.com/roles/?level__gte=100&level__lt=1000&book_id=4&type=Wizard
# - дать роли книги 4, с типом Wizard, уровнями от 100 до 1000 (не включительно).

import unittest
import requests


class FiltersTests(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://pulse-rest-testing.herokuapp.com/roles/"

    def test_get_roles_from_book(self):
        response = requests.get(self.base_url, params={'book_id': 1})
        self.assertEqual(response .status_code, 200)
        resp_dict = response.json()
        for book in resp_dict:
            self.assertIn("id", book)
            self.assertIn("name", book)
            self.assertIn("type", book)
            self.assertIn("book", book)
