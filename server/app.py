# server/app.py

from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, User, Review, Game

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def index():
    return "Index for Game/Review/User API"


@app.route('/games')
def games():
    games = []
    for game in Game.query.order_by(Game.title).all():
        game_dict = {
            'title': game.title,
            'genre': game.genre,
            'platform': game.platform,
            'price': game.price
        }
        games.append(game_dict)

    return games


if __name__ == '__main__':
    app.run(port=5555, debug=True)
