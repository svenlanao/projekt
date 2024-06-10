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

