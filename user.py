from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/FlipDeck_name'
db = SQLAlchemy(app)


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False)
    password_hash = db.Column(db.String(256))
    email = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self, name, password, email):
        self.name = name
        self.email = email
        self.set_password(password)

    def set_password(self, password):
        # Generate a salt and hash the password
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        self.password_hash = hashed_password.decode('utf-8')

    def check_password(self, password):
        # Check if the provided password matches the hashed password
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

    @classmethod
    def get_user_by_name(cls, name):
        # Retrieve a user by name using a parameterized query
        return cls.query.filter_by(name=name).first()

    # Route for registering a user


@app.route('/register', methods=['POST'])
def register():
    # Retrieve user data from the request
    name = request.json['name']
    password = request.json['password']
    email = request.json['email']

    # Check if a user with the same name already exists
    existing_user = User.get_user_by_name(name)
    if existing_user:
        return jsonify({'message': 'Username already exists'})

    # Create a new user object
    new_user = User(name=name, password=password, email=email)

    # Save the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'})

if __name__ == '__main__':
    app.run()
