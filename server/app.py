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
    return [game.to_dict() for game in Game.query.all()]


@app.route('/games/<int:id>')
def game_by_id(id):
    game = Game.query.get(id)
    return game.to_dict()


if __name__ == '__main__':
    app.run(port=5555, debug=True)
