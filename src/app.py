# Importing the os module.
import os

# Importing the Flask, jsonify, and render_template modules from the flask package.
from flask import Flask, jsonify, render_template

# Importing the config, Company, Games, and Routes variables from the config.py, db_company.py,
# db_games.py, and routes.py files.
from config import config
from database.db_company import Company
from database.db_games import Games
from routes import Routes

# Creating a Flask object.
app = Flask(__name__)

# Taking all the files in the IMG folder and putting them in a list.
IMG_LIST = os.listdir('src/static/IMG')
# Joining the static folder and the IMG folder together.
IMG_FOLDER = os.path.join('static', 'IMG')
# Setting the upload folder to the IMG_FOLDER variable.
app.config['UPLOAD_FOLDER'] = IMG_FOLDER


@app.route('/')
def home():
    """
    It returns a JSON object with a key of "Routes" and a value of the Routes variable.
    :return: A dictionary with a key of "Routes" and a value of the Routes variable.
    """
    return jsonify({"Routes": Routes})


@app.route('/games')
def getGames():
    """
    It takes the list of games and returns it as a JSON object
    :return: A JSON object with a key of "Games" and a value of the Games list.
    """
    return jsonify({"Games": Games})


@app.route('/games/<int:id>')
def getGame(id):
    """
    If the game exists, return the game, otherwise return a message saying the game doesn't exist

    :param id: The id of the game you want to retrieve
    :return: A list of games that have the same id as the id passed in.
    """
    foundGame = [game for game in Games if game['id'] == id]
    if (len(foundGame) > 0):
        return jsonify({"game": foundGame[0]})
    return jsonify({"message": "game not found"})


@app.route('/companies')
def getCompanies():
    """
    It takes the Company variable, which is a list of dictionaries, and returns it as a JSON object.
    :return: A dictionary with a key of "companies" and a value of the Company class.
    """
    return jsonify({"companies": Company})


@app.route('/companies/<int:id>')
def getCompany(id):
    """
    It takes an id as a parameter, searches the Company list for a company with that id, and returns the
    company if it exists, or a message if it doesn't

    :param id: The id of the company you want to retrieve
    :return: A list of dictionaries.
    """
    foundCompany = [company for company in Company if company['id'] == id]
    if (len(foundCompany) > 0):
        return jsonify({"company": foundCompany[0]})
    return jsonify({"message": "company not found"})


@app.route('/photos')
def getPhotos():
    """
    It takes all the files in the IMG folder and puts them in a list.
    :return: The photos.html template is being returned.
    """
    IMG_LIST = os.listdir('src/static/IMG')
    IMG_LIST = ['IMG/' + i for i in IMG_LIST]
    return render_template("photos.html", imagelist=IMG_LIST)


@app.errorhandler(404)
def urlNotFound(e):
    return jsonify({"Message": "Url not found"})


# Running the app.
if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()
