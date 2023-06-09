from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import bcrypt

from flask import render_template
from app import create_app

db = SQLAlchemy()
app = create_app()

# Define the Flashcard model


class Flashcard(db.Model):
    flashcard_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    front_text = db.Column(db.String(256))
    back_text = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now)
    deck_id = db.Column(db.Integer, db.ForeignKey('deck.deck_id'))

    def __init__(self, front_text, back_text, deck_id):
        self.front_text = front_text
        self.back_text = back_text
        self.deck_id = deck_id


# Route for creating a flashcard
@app.route('/flashcard')
def new_flashcard():
    return render_template('flashcard.html')

@app.route('/flashcards', methods=['POST'])
def create_flashcard():
    # Retrieve flashcard data from the request
    front_text = request.form['Question']
    back_text = request.form['answer']
    explanation = request.form['Explanation']
    deck_id = request.json['deck_id']

    # Create a new flashcard object
    new_flashcard = Flashcard(front_text=front_text,
                              back_text=back_text, explanation=explanation, deck_id=deck_id)

    # Save the new flashcard to the database
    db.session.add(new_flashcard)
    db.session.commit()

    return jsonify({'message': 'Flashcard created successfully'})


if __name__ == '__main__':
    app.run()
