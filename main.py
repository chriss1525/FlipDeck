from Deck import create_deck
from Flashcards import create_flashcard
from progress import create_progress
from user import register
from Deck import Deck
from Flashcards import Flashcard
from progress import Progress
from user import User
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/FlipDeck_name'
db = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/deck')
def deck():
    return render_template('deck.html')

@app.route('/create_deck')
def create_deck():
    return render_template('create_deck.html')

@app.route('/answer')
def answer():
    return render_template('answer.html')

app.add_url_rule('/register', methods=['POST'], view_func=register)
app.add_url_rule('/progress', methods=['POST'], view_func=create_progress)
app.add_url_rule('/flashcards', methods=['POST'], view_func=create_flashcard)
app.add_url_rule('/decks', methods=['POST'], view_func=create_deck)

if __name__ == '__main__':
    app.run()
