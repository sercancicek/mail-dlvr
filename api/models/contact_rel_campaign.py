from api import db


class ContactRelCampaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer)
    contact_id = db.Column(db.Integer)
    sent_date = db.Column(db.DateTime())
    clicked_date = db.Column(db.DateTime())

    def __init__(self, campaign_id, contact_id):
        self.campaign_id = campaign_id
        self.contact_id = contact_id

    def __repr__(self):
        return f'campaign_id: ${self.campaign_id} - contact_id ${self.contact_id}'


