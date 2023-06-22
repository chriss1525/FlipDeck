#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template
from flask_login import login_required, current_user

routes = Blueprint('routes', __name__)

@routes.route('/')
@login_required
def home():
    return render_template('homepage.html', user=current_user)

@routes.route('/deck')
def deck():
    return render_template('deck.html', user=current_user)

@routes.route('/create_deck')
def create_deck():
    return render_template('create_deck.html', user=current_user)
