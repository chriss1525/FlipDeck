from Deck import create_deck
from Flashcards import create_flashcard
from progress import create_progress
from user import register
from Deck import Deck
from Flashcards import Flashcard
from progress import Progress
from user import User
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/FlipDeck_name'
db = SQLAlchemy(app)

# Import the models

# Import the routes

# Add the routes to the Flask app


@app.route('/')
def home():
    return 'Welcome to the home page!'


app.add_url_rule('/register', methods=['POST'], view_func=register)
app.add_url_rule('/progress', methods=['POST'], view_func=create_progress)
app.add_url_rule('/flashcards', methods=['POST'], view_func=create_flashcard)
app.add_url_rule('/decks', methods=['POST'], view_func=create_deck)

if __name__ == '__main__':
    app.run()
