from flask import Blueprint, render_template, request
from .models import db, Autor, Buch, Genre, Subgenre

main_routes = Blueprint('main_routes', __name__)

#Homepage
@main_routes.route('/')
def home():
    return render_template('home.html')

#Autoren 
@main_routes.route('/autoren')
def autoren():
    nationalitat = request.args.get('nationalitat')
    if nationalitat:
        autoren = Autor.query.filter_by(nationalitat=nationalitat).all()
    else:
        autoren = Autor.query.all()
    return render_template('autoren.html', autoren=autoren)

#Bucher
@main_routes.route('/bucher')
def bucher():
    subgenre = request.args.get('subgenre')
    if subgenre:
        bucher = Buch.query.join(Subgenre).filter(Subgenre.subgenre==subgenre).all()
    else:
        bucher = Buch.query.all()
    
    order = request.args.get('order', default=None)
    if order == 'desc':
        bucher = Buch.query.order_by(Buch.preis.desc()).all()
    elif order == 'asc':
        bucher = Buch.query.order_by(Buch.preis.asc()).all()
    return render_template('bucher.html', bucher=bucher, order=order)

#Genre
@main_routes.route('/genres')
def genre_subgenre():
    genres = Genre.query.all()
    return render_template('genre_subgenre.html', genres=genres)


#



