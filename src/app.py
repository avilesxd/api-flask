from flask import Flask, jsonify

from config import config
from database.db_company import Company
from database.db_games import Games
from routes import Routes

app = Flask(__name__)


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


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()
