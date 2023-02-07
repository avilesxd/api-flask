import random
import unittest
import requests

from flask import Flask
app = Flask(__name__)


class TestAPI(unittest.TestCase):

    def test_route_to_get_the_games(self):
        req = requests.get("http://127.0.0.1:5000/games")
        self.assertEqual(req.status_code, 200)

    def test_route_to_get_the_specific_game(self):
        id = random.randint(1, 10)
        req = requests.get(f"http://127.0.0.1:5000/games/{id}")
        self.assertEqual(req.status_code, 200)

    def test_route_to_get_the_companies(self):
        req = requests.get("http://127.0.0.1:5000/companies")
        self.assertEqual(req.status_code, 200)

    def test_route_to_get_the_specific_company(self):
        id = random.randint(1, 2)
        req = requests.get(f"http://127.0.0.1:5000/companies/{id}")
        self.assertEqual(req.status_code, 200)

    def test_route_to_get_the_photos(self):
        req = requests.get("http://127.0.0.1:5000/photos")
        self.assertEqual(req.status_code, 200)

    def test_route_not_exists(self):
        with app.test_client() as c:
            response = c.get('http://127.0.0.1:5000/copanies/42')
            self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
