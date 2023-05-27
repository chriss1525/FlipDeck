from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/FlipDeck_name'
db = SQLAlchemy(app)

# Define the Deck model


class Deck(db.Model):
    deck_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(256))
    description = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.user_id = user_id

# Route for creating a deck


@app.route('/decks', methods=['POST'])
def create_deck():
    # Retrieve deck data from the request
    title = request.json['title']
    description = request.json['description']
    user_id = request.json['user_id']

    # Create a new deck object
    new_deck = Deck(title=title, description=description, user_id=user_id)

    # Save the new deck to the database
    db.session.add(new_deck)
    db.session.commit()

    return jsonify({'message': 'Deck created successfully'})


if __name__ == '__main__':
    app.run()
