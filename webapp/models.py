#!/usr/bin/env python
# -*- coding: utf-8 -*-


from . import db
from flask_login import UserMixin
from sqlalchemy import func


class Deck(db.Model):
    __tablename__ = 'deck'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    card_count = db.Column(db.Integer, default=0)
    card = db.relationship('Card')


class Card(db.Model):
    __tablename__ = 'card'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(100))
    answer = db.Column(db.String(200))
    explanation = db.Column(db.String(10000))
    deck_id = db.Column(db.Integer, db.ForeignKey('deck.id')) 


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    decks = db.relationship('Deck')

