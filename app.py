from application import user #Deck, Flashcards, progress, user
#from application.Deck import create_deck
#from application.Flashcards import create_flashcard
#from application.progress import create_progress
from application.user import register
from application.user import login
#from application.Deck import Deck
#from application.Flashcards import Flashcard
#from application.progress import Progress
from application.user import User
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/homepage2')
def home2():
    return render_template('homepage2.html')

@app.route('/deck')
def deck():
   return render_template('deck.html')

@app.route('/create_deck')
def create_deck():
    return render_template('create_deck.html')


@app.route('/answer')
def answer():
    return render_template('answer.html')

@app.route('/flashcards')
def flashcards():
    return render_template('flashcards.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

app.add_url_rule('/register', methods=['POST'], view_func=register)
app.add_url_rule('/login', methods=['POST'], view_func=login)
#app.add_url_rule('/progress', methods=['POST'], view_func=create_progress)
#app.add_url_rule('/flashcards', methods=['POST'], view_func=create_flashcard)
#app.add_url_rule('/decks', methods=['POST'], view_func=create_deck)

if __name__ == '__main__':
    app.run(debug=True)
