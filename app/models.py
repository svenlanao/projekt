from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Autor(db.Model):
    __tablename__ = 'tbl_autor'

    autor_id = db.Column(db.SmallInteger, primary_key=True)
    name = db.Column(db.String(30))
    nationalitat = db.Column(db.String(30))
    genre_id = db.Column(db.SmallInteger)

    def __repr__(self):
        return f'<Autor {self.name}>'

class Buch(db.Model):
    __tablename__='tbl_buch'
    buch_id=db.Column(db.SmallInteger, primary_key=True)
    isbn=db.Column(db.BigInteger)
    titel=db.Column(db.String(80))
    subgen_id=db.Column(db.SmallInteger)
    verlag=db.Column(db.String(40))
    veroffentlichungsdatum=db.Column(db.Date)
    preis=db.Column(db.Numeric(precision=4, scale=2))

    def __repr__(self):
        return f'<Autor {self.titel}>'