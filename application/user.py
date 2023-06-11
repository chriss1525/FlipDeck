from flask import Flask, request, jsonify, redirect, render_template
from datetime import datetime
import bcrypt
import json
import os
from flask_login import LoginManager, UserMixin, login_user, login_required

app = Flask(__name__)
app.secret_key = "where do I get this?"

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


class User(UserMixin):
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
        # Retrieve a user by name from the JSON file
        if not os.path.isfile('data.json'):
            # If the file doesn't exist, create an empty JSON structure
            with open('data.json', 'w') as file:
                json.dump({'users': []}, file)
        # Retrieve a user by name from the JSON file
        with open('data.json', 'r') as file:
            data = json.load(file)
        for user_data in data['users']:
            if user_data['name'] == name:
                return cls(name=user_data['name'], password=user_data['password'], email=user_data['email'])
        return None


    @classmethod
    def get_user_by_email(cls, email):
        # Retrieve a user by email from the JSON file
        if not os.path.isfile('data.json'):
            # If the file doesn't exist, create an empty JSON structure
            with open('data.json', 'w') as file:
                json.dump({'users': []}, file)
        # Retrieve a user by email from the JSON file
        with open('data.json', 'r') as file:
            data = json.load(file)
        for user_data in data['users']:
            if user_data['email'] == email:
                return cls(name=user_data['name'], password=user_data['password'], email=user_data['email'])
        return None


    def save(self):
        # Save the user to the JSON file
        with open('data.json', 'r') as file:
            data = json.load(file)
        user_data = {
            'name': self.name,
            'password': self.password_hash,
            'email': self.email
        }
        data['users'].append(user_data)
        with open('data.json', 'w') as file:
            json.dump(data, file)

    # Route for registering a user


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        # Retrieve user data from the request
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']

        # Check if a user with the same name already exists
        existing_user = User.get_user_by_name(name)
        if existing_user:
            return render_template('signup.html', message='Username already exists')

        # Check if a user with the same email already exists
        existing_email = User.get_user_by_email(email)
        if existing_email:
            return render_template('signup.html', message='Password already exists')

        # Create a new user object
        new_user = User(name=name, password=password, email=email)

        # Save the new user to the JSON file
        new_user.save()
        return redirect('homepage2')
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        remember_me = request.form.get('remember_me')
        
        user = User.get_user_by_name(name)
        
        if user and user.check_password(password):
            login_user(user, remember=remember_me)
            return redirect('homepage2')
        
    return render_template('signup.html', message='Invalid username or password')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

def get_user_by_name(name):
    # Load the users from the JSON file
    users = load_users()

    # Find the user with the matching name
    for user in users:
        if user['name'] == name:
            return user

        return None

#def load_users():
 #   with open('data.json', 'r') as file:
  #      users = json.load(file)
   # return users

@login_manager.user_loader
def load_user(user_id):
    return User.get_user_by_name(user_id)   

def save_user(user):
    # Load the existing users from the JSON file
    users = load_users()

    # Add the new user to the list
    users.append(user)

    # Save the updated users list to the JSON file
    with open('data.json', 'w') as file:
        json.dump(users, file)

if __name__ == '__main__':
    app.run(debug=True)
