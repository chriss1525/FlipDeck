#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Deck
from . import db

routes = Blueprint('routes', __name__)

@routes.route('/')
@login_required
def home():
    return render_template('homepage.html', user=current_user)

@routes.route('/deck')
@login_required
def deck():
    # Retrieve user's decks from database
    user_decks = Deck.query.filter_by(user_id=current_user.id).all()
    return render_template('deck.html', deck=user_decks, user=current_user)

@routes.route('/decks/create', methods=['GET', 'POST'])
@login_required
def create_deck():
    # get title from form
    if request.method == 'POST':
        title = request.form['Topic']

        # create new deck object
        new_deck = Deck(title=title, user_id=current_user.id)
        db.session.add(new_deck)
        db.session.commit()

        print(new_deck)

        # redirect to deck page
        return redirect(url_for('routes.deck'))
    return render_template('create_deck.html', user=current_user)
