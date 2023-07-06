#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Deck, Card
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

        # Generate new static folder path based on deck id
        #new_deck.static_path = 'static/decks/' + str(new_deck.id)

        # redirect to deck page
        return redirect(url_for('routes.flashcard', id=new_deck.id))
    return render_template('create_deck.html', user=current_user)

@routes.route('/decks/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def delete_deck(id):
    # get deck id from url
    deck = Deck.query.get_or_404(id)

    # delete deck from database
    db.session.delete(deck)
    db.session.commit()

    # redirect to deck page
    return redirect(url_for('routes.deck'))

@routes.route('/decks/<int:id>/flashcards')
@login_required
def flashcard(id):
    # Retrieve user's decks from database
    user_flashcards = Deck.query.filter_by(user_id=current_user.id).all()
    return render_template('flashcards.html', flashcards=user_flashcards)

@routes.route('/decks/<int:id>/flashcards/create', methods=['GET', 'POST'])
@login_required
def create_flashcard(id):
    # Retrieve the deck from the database based on the provided ID
    deck = Deck.query.get_or_404(id)

    if request.method == 'POST':
        question = request.form['Question']
        answer = request.form['Answer']
        explanation = request.form['Explanation']

        # Create a new card object
        new_card = Card(question=question, answer=answer, explanation=explanation, deck_id=deck.id)

        # Add the card to the deck
        deck.card.append(new_card)

        # Update the card count
        deck.card_count = len(deck.card)

        # Commit changes to the database
        db.session.commit()

        # Redirect to the flashcards page
        return redirect(url_for('routes.flashcards', id=deck.id))

    return render_template('create_flashcards.html', deck=deck, user=current_user)

@routes.route('/decks/<int:id>/flashcards/<int:card_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_flashcard(id, card_id):
    # Retrieve the card from the database based on the provided ID
    card = Card.query.get_or_404(card_id)

    # Delete the card from the database
    db.session.delete(card)
    db.session.commit()

    # Redirect to the flashcards page
    return redirect(url_for('routes.flashcards'))

@routes.route('/decks/<int:id>/flashcards/<int:card_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_flashcard(id, card_id):
    # Retrieve the card from the database based on the provided ID
    card = Card.query.get_or_404(card_id)

    if request.method == 'POST':
        card.question = request.form['Question']
        card.answer = request.form['Answer']
        card.explanation = request.form['Explanation']

        # Commit changes to the database
        db.session.commit()

        # Redirect to the flashcards page
        return redirect(url_for('routes.flashcards'))

    return render_template('edit_flashcard.html', card=card, user=current_user)
