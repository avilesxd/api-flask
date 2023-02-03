import random
import unittest
import requests


class TestAPI(unittest.TestCase):

    def test_route_to_get_the_games(self):
        req = requests.get("http://127.0.0.1:5000/games")
        print(f"Games route:", req.status_code)
        self.assertEqual(req.status_code, 200)

    def test_route_to_get_the_specific_game(self):
        id = random.randint(1, 10)
        req = requests.get(f"http://127.0.0.1:5000/games/{id}")
        print(f"game path with unique id:", req.status_code)
        self.assertEqual(req.status_code, 200)

    def test_route_to_get_the_companies(self):
        req = requests.get("http://127.0.0.1:5000/companies")
        print(f"Companies route:", req.status_code)
        self.assertEqual(req.status_code, 200)

    def test_route_to_get_the_company(self):
        id = random.randint(1, 2)
        req = requests.get(f"http://127.0.0.1:5000/companies/{id}")
        print(f"company path with unique id:", req.status_code)
        self.assertEqual(req.status_code, 200)

    def test_route_to_get_the_photos(self):
        req = requests.get("http://127.0.0.1:5000/photos")
        print(f"Photos route:", req.status_code)
        self.assertEqual(req.status_code, 200)


if __name__ == "__main__":
    unittest.main()
