from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Autor(db.Model):
    __tablename__ = 'tbl_autor'

    autor_id = db.Column(db.SmallInteger, primary_key=True)
    name = db.Column(db.String(30))
    nationalitat = db.Column(db.String(30))
    genre_id = db.Column(db.SmallInteger, db.ForeignKey('tbl_genre.genre_id'))
    genre = db.relationship('Genre', backref='autoren')

    def __repr__(self):
        return f'<Autor {self.name}>'

class Buch(db.Model):
    __tablename__='tbl_buch'
    buch_id=db.Column(db.SmallInteger, primary_key=True)
    isbn=db.Column(db.BigInteger)
    titel=db.Column(db.String(80))
    subgen_id=db.Column(db.SmallInteger, db.ForeignKey('tbl_subgenre.subgen_id'))
    verlag=db.Column(db.String(40))
    veroffentlichungsdatum=db.Column(db.Date)
    preis=db.Column(db.Numeric(precision=4, scale=2))
    #genre=db.relationship('Genre', backref='bucher')
    subgenre=db.relationship('Subgenre', backref='bucher', lazy=True)

    def __repr__(self):
        return f'<Autor {self.titel}>'
    
class Genre(db.Model):
    __tablename__='tbl_genre'
    genre_id=db.Column(db.SmallInteger, primary_key=True)
    genre=db.Column(db.String(25))
    subgenres = db.relationship('Subgenre', backref='parent_genre', lazy=True)
    
    def __repr__(self):
        return f'<Genre {self.genre}>'
    
class Subgenre(db.Model):
    __tablename__='tbl_subgenre'
    subgen_id=db.Column(db.SmallInteger, primary_key=True)
    subgenre=db.Column(db.String(25))
    genre_id=db.Column(db.SmallInteger, db.ForeignKey('tbl_genre.genre_id'))
    genre=db.relationship('Genre', backref='child_subgenres', lazy=True)
    
    def __repr__(self):
        return f'<Subgenre {self.subgenre}>'