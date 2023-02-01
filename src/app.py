import os
from flask import Flask, jsonify, render_template

from config import config
from database.db_company import Company
from database.db_games import Games
from routes import Routes

app = Flask(__name__)

IMG_LIST = os.listdir('src/static/IMG')
IMG_FOLDER = os.path.join('static', 'IMG')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER


@app.route('/')
def home():
    return jsonify({"Routes": Routes})


@app.route('/games')
def getGames():
    return jsonify({"Games": Games})


@app.route('/games/<int:id>')
def getGame(id):
    foundGame = [game for game in Games if game['id'] == id]
    if (len(foundGame) > 0):
        return jsonify({"game": foundGame[0]})
    return jsonify({"message": "game not found"})


@app.route('/companies')
def getCompanies():
    return jsonify({"companies": Company})


@app.route('/companies/<int:id>')
def getCompany(id):
    foundCompany = [company for company in Company if company['id'] == id]
    if (len(foundCompany) > 0):
        return jsonify({"company": foundCompany[0]})
    return jsonify({"message": "company not found"})


@app.route('/photos')
def getPhotos():
    IMG_LIST = os.listdir('src/static/IMG')
    IMG_LIST = ['IMG/' + i for i in IMG_LIST]
    return render_template("photos.html", imagelist=IMG_LIST)


@app.errorhandler(404)
def pageNotFound(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()
