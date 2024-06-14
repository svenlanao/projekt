from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Autor, Buch, Genre, Subgenre

main_routes = Blueprint('main_routes', __name__)

rechner = {}

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
        bucher = Buch.query.join(Subgenre).filter(Subgenre.subgenre == subgenre).all()
    else:
        bucher = Buch.query.all()
    
    order = request.args.get('order', default=None)
    if order == 'desc':
        bucher = sorted(bucher, key=lambda x: x.preis, reverse=True)
    elif order == 'asc':
        bucher = sorted(bucher, key=lambda x: x.preis)
    return render_template('bucher.html', bucher=bucher, order=order, rechner=rechner, total_price=gesamtsumme_berechnen())

#Aus dem Rechner entfernen
@main_routes.route('/aus_dem_rechner_entfernen/<int:book_id>', methods = ['POST'])
def enfernen(book_id):
    if book_id in rechner:
        del rechner[book_id]
    return redirect(url_for('main_routes.bucher'))

#Zur Rechner hinzufügen
@main_routes.route('/zur_rechner_addieren/<int:book_id>', methods=['POST'])
def addieren(book_id):
    menge = int(request.form['menge'])
    if book_id in rechner:
        rechner[book_id]['quantity'] += menge
    else:
        book = Buch.query.get(book_id)
        rechner[book_id] = {'book_titel':book.titel, 'quantity':menge, 'price':book.preis}
    return redirect(url_for('main_routes.bucher'))

@main_routes.route('/mehrfache_addieren', methods=['POST'])
def mehrfache_addieren():
    selected_books = request.form.getlist('selected_books')
    for book_id in selected_books:
        book_id = int(book_id)
        menge = int(request.form.get(f'menge_{book_id}', 1))
        if book_id in rechner:
            rechner[book_id]['quantity'] += menge
        else:
            book = Buch.query.get(book_id)
            rechner[book_id] = {'book_titel': book.titel, 'quantity': menge, 'price': book.preis}
    return redirect(url_for('main_routes.bucher'))

#Menge aktualisieren
@main_routes.route('/menge_aktualisieren/<int:book_id>', methods=['POST'])
def aktualisieren(book_id):
    menge = int(request.form['menge'])
    if book_id in rechner:
        rechner[book_id]['quantity'] = menge
    return redirect(url_for('main_routes.bucher'))

#Gesamtsumme berechnen
def gesamtsumme_berechnen():
    total = 0
    for book_id, book_data in rechner.items():
        total += book_data['price'] * book_data['quantity']
    return total

#Genre
@main_routes.route('/genres')
def genre_subgenre():
    genres = Genre.query.all()
    return render_template('genre_subgenre.html', genres=genres)

