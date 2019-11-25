from api import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    email = db.Column(db.String(250), unique=True)

    def __init__(self, full_name, email):
        self.full_name = full_name
        self.email = email

    def __repr__(self):
        return f'ID: ${self.id} - Full Name: ${self.full_name} - E-Mail: ${self.email}'


