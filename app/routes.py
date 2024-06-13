from flask import Blueprint, render_template, request
from .models import db, Autor, Buch, Genre

main_routes = Blueprint('main_routes', __name__)

#Homepage
@main_routes.route('/')
def home():
    return render_template('home.html')

#Autoren 
@main_routes.route('/autoren')
def autoren():
    autoren = Autor.query.all()
    return render_template('autoren.html', autoren=autoren)

#Bucher
@main_routes.route('/bucher')
def bucher():
    bucher = Buch.query.all()
    return render_template('bucher.html', bucher=bucher)

#Genre
@main_routes.route('/genres')
def genre_subgenre():
    genres = Genre.query.all()
    return render_template('genre_subgenre.html', genres=genres)



