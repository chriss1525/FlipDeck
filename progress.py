from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/FlipDeck_name'
db = SQLAlchemy(app)

# Define the Progress model


class Progress(db.Model):
    progress_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False)
    password_hash = db.Column(db.String(256))
    email = db.Column(db.String(256))
    last_viewed = db.Column(db.DateTime)
    completed = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    flashcard_id = db.Column(
        db.Integer, db.ForeignKey('flashcards.flashcard_id'))

    def __init__(self, name, password_hash, email, last_viewed, completed, user_id, flashcard_id):
        self.name = name
        self.password_hash = password_hash
        self.email = email
        self.last_viewed = last_viewed
        self.completed = completed
        self.user_id = user_id
        self.flashcard_id = flashcard_id

# Route for creating progress


@app.route('/progress', methods=['POST'])
def create_progress():
    # Retrieve progress data from the request
    name = request.json['name']
    password_hash = request.json['password_hash']
    email = request.json['email']
    last_viewed = request.json['last_viewed']
    completed = request.json['completed']
    user_id = request.json['user_id']
    flashcard_id = request.json['flashcard_id']

    # Create a new progress object
    new_progress = Progress(name=name, password_hash=password_hash, email=email,
                            last_viewed=last_viewed, completed=completed,
                            user_id=user_id, flashcard_id=flashcard_id)

    # Save the new progress to the database
    db.session.add(new_progress)
    db.session.commit()

    return jsonify({'message': 'Progress created successfully'})


if __name__ == '__main__':
    app.run()
