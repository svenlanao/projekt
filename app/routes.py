from flask import Blueprint, render_template, request
from .models import db, Autor

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
def index():
    autoren = Autor.query.all() #fehler
    return render_template('index.html', autoren=autoren)

@main_routes.route('/suchen', methods=['GET', 'POST'])
def suchen():
    if request.method == 'POST':
        name = request.form.get('name')
        autoren = Autor.query.filter(Autor.name.ilike(f'%{name}%')).all()
    else:
        autoren = Autor.query.all()
    return render_template('buscar.html', autoren=autoren)


