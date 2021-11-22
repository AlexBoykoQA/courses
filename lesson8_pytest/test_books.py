import pytest
import requests


base_url = "http://pulse-rest-testing.herokuapp.com/"

book_data = {"title": "Anna Karenina", "author": "Lev Tolstoy"}
updated_data = {"title": "JAVA"}


@pytest.fixture
def book():
    response = requests.post(base_url + "books/", data=book_data)
    assert response.status_code == 201
    json_data = response.json()
    yield json_data
    book_id = json_data["id"]
    response = requests.delete(base_url + "books/" + str(book_id))


class TestsBook:
    def test_create_book(self):
        response = requests.post(base_url + "books", data=book_data)
        assert response.status_code == 201
        json_data = response.json()
        book_id = json_data["id"]
        for item in book_data:
            assert item in json_data
            assert book_data[item] == json_data[item]
        response = requests.delete(base_url + "books/" + str(book_id))

    def test_get_book(self, book):
        response = requests.get(base_url + "books/" + str(book["id"]))
        # print(response.request.url)
        assert response.status_code == 200
        resp_dict = response.json()
        assert "id" in resp_dict
        assert "title" in resp_dict
        assert "author" in resp_dict

    def test_get_books(self):
        response = requests.get(base_url + "books/")
        # print(response.request.url)
        assert response.status_code == 200
        resp_dict = response.json()
        for book in resp_dict:
            assert "id" in book
            assert "title" in book
            assert "author" in book

    def test_update_book(self, book):
        response = requests.put(base_url + "books/" + str(book["id"]), data=updated_data)
        # print(response.request.url)
        assert response.status_code == 200
        resp_dict = response.json()
        assert resp_dict["title"] == updated_data["title"]

    def test_delete_book(self, book):
        response = requests.delete(base_url + "books/" + str(book["id"]))
        assert response.status_code == 204
