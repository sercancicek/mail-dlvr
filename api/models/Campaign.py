from api import db


class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(500))

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return f'ID: ${self.id} - Title: ${self.title} - Description: ${self.description}'
