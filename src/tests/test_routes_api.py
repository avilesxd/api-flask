# Importing the modules that are needed for the test.
import random
import unittest
import requests


# Importing the Flask module.
from flask import Flask
# Creating a Flask application object.
app = Flask(__name__)


# It tests the API routes to see if they are working properly
class TestAPI(unittest.TestCase):

    def test_route_to_get_the_games(self):
        """
        It tests that the route /games returns a 200 status code
        """
        req = requests.get("http://127.0.0.1:5000/games")
        self.assertEqual(req.status_code, 200)

    def test_route_to_get_the_specific_game(self):
        """
        It tests the route to get the specific game.
        """
        id = random.randint(1, 10)
        req = requests.get(f"http://127.0.0.1:5000/games/{id}")
        self.assertEqual(req.status_code, 200)

    def test_route_to_get_the_companies(self):
        """
        It tests the route to get the companies.
        """
        req = requests.get("http://127.0.0.1:5000/companies")
        self.assertEqual(req.status_code, 200)

    def test_route_to_get_the_specific_company(self):
        """
        It tests if the route to get the specific company is working.
        """
        id = random.randint(1, 2)
        req = requests.get(f"http://127.0.0.1:5000/companies/{id}")
        self.assertEqual(req.status_code, 200)

    def test_route_to_get_the_photos(self):
        """
        It tests the route to get the photos.
        """
        req = requests.get("http://127.0.0.1:5000/photos")
        self.assertEqual(req.status_code, 200)

    def test_route_not_exists(self):
        """
        It creates a test client, uses it to make a request to the server, 
        and then asserts that the response status code is 404
        """
        with app.test_client() as c:
            response = c.get('http://127.0.0.1:5000/copanies/42')
            self.assertEqual(response.status_code, 404)


# Running the tests.
if __name__ == "__main__":
    unittest.main()
