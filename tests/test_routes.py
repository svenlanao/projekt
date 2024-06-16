import unittest
import sys
from pathlib import Path
from flask_testing import TestCase
from flask import url_for

# Füge das Projektverzeichnis zum sys.path hinzu
sys.path.append(str(Path(__file__).resolve().parents[1]))

from app import create_app, db  # Importiere create_app und db von app
from app.models import Buch  # Importiere die benötigten Modelle von app.models
from app.routes import main_routes  # Importiere main_routes von app.routes

class TestAddieren(TestCase):

    def create_app(self):
        # Konfiguriere die Anwendung für Tests
        app = create_app('testing')
        
        # Überprüfe, ob der Blueprint bereits registriert ist
        if 'main_routes' not in app.blueprints:
            app.register_blueprint(main_routes)  # Registriere den Blueprint
        return app

    def setUp(self):
        # Bereite die Datenbank vor jedem Test vor
        db.create_all()
        # Füge ein Testbuch hinzu
        self.book = Buch(titel="Test Buch", preis=20.00)
        db.session.add(self.book)
        db.session.commit()

    def tearDown(self):
        # Bereinige die Datenbank nach jedem Test
        db.session.remove()
        db.drop_all()

    def test_addieren_success(self):
        # Teste das erfolgreiche Hinzufügen eines Buches
        response = self.client.post(url_for('main_routes.addieren', book_id=self.book.buch_id), data={'menge': 2})
        self.assertEqual(response.status_code, 302)
        self.assertIn(self.book.buch_id, self.app.rechner)
        self.assertEqual(self.app.rechner[self.book.buch_id]['quantity'], 2)

    def test_addieren_increment(self):
        # Teste die Erhöhung der Menge eines vorhandenen Buches
        self.app.rechner[self.book.buch_id] = {'book_titel': self.book.titel, 'quantity': 1, 'price': self.book.preis}
        response = self.client.post(url_for('main_routes.addieren', book_id=self.book.buch_id), data={'menge': 2})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.app.rechner[self.book.buch_id]['quantity'], 3)

    def test_addieren_invalid_book_id(self):
        # Teste das Hinzufügen eines Buches mit ungültiger ID
        response = self.client.post(url_for('main_routes.addieren', book_id=9999), data={'menge': 2})
        self.assertEqual(response.status_code, 404)

    def test_addieren_no_quantity(self):
        # Teste das Hinzufügen eines Buches ohne Angabe der Menge
        response = self.client.post(url_for('main_routes.addieren', book_id=self.book.buch_id), data={})
        self.assertEqual(response.status_code, 400)

    def test_addieren_zero_quantity(self):
        # Teste das Hinzufügen eines Buches mit Menge null
        response = self.client.post(url_for('main_routes.addieren', book_id=self.book.buch_id), data={'menge': 0})
        self.assertEqual(response.status_code, 400)

    def test_addieren_negative_quantity(self):
        # Teste das Hinzufügen eines Buches mit negativer Menge
        response = self.client.post(url_for('main_routes.addieren', book_id=self.book.buch_id), data={'menge': -1})
        self.assertEqual(response.status_code, 400)

    def test_addieren_non_integer_quantity(self):
        # Teste das Hinzufügen eines Buches mit nicht ganzzahliger Menge
        response = self.client.post(url_for('main_routes.addieren', book_id=self.book.buch_id), data={'menge': 'two'})
        self.assertEqual(response.status_code, 400)

    def test_addieren_exceed_stock(self):
        # Teste das Hinzufügen eines Buches, das den verfügbaren Lagerbestand überschreitet (falls zutreffend)
        # Angenommen, der verfügbare Lagerbestand beträgt 5
        self.book.stock = 5
        db.session.commit()
        response = self.client.post(url_for('main_routes.addieren', book_id=self.book.buch_id), data={'menge': 10})
        self.assertEqual(response.status_code, 400)

    def test_addieren_success_with_different_books(self):
        # Teste das gleichzeitige Hinzufügen verschiedener Bücher
        book2 = Buch(titel="Anderes Buch", preis=15.00)
        db.session.add(book2)
        db.session.commit()
        response = self.client.post(url_for('main_routes.addieren', book_id=self.book.buch_id), data={'menge': 2})
        response2 = self.client.post(url_for('main_routes.addieren', book_id=book2.buch_id), data={'menge': 3})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response2.status_code, 302)
        self.assertIn(self.book.buch_id, self.app.rechner)
        self.assertIn(book2.buch_id, self.app.rechner)
        self.assertEqual(self.app.rechner[self.book.buch_id]['quantity'], 2)
        self.assertEqual(self.app.rechner[book2.buch_id]['quantity'], 3)

    def test_addieren_clear_rechner(self):
        # Teste das Löschen des "Rechners"
        self.app.rechner = {self.book.buch_id: {'book_titel': self.book.titel, 'quantity': 2, 'price': self.book.preis}}
        response = self.client.post(url_for('main_routes.enfernen', book_id=self.book.buch_id))
        self.assertEqual(response.status_code, 302)
        self.assertNotIn(self.book.buch_id, self.app.rechner)


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
