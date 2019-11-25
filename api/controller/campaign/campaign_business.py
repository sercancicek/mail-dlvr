from datetime import datetime

from flask import request

from api import db
from api.models.Campaign import Campaign
from api.models.contact_rel_campaign import ContactRelCampaign


def get_campaign_params_from_request():
    return request.json['title'], request.json['desc']


def get_campaign_contact_params_from_request():
    return request.json['contacts']


def get_publish_campaign_params_from_request():
    return request.json['text']


def get_file_param_from_request():
    return request.files['file']


def save_campaign_to_db(new_campaign):
    try:
        db.session.add(new_campaign)
        db.session.commit( )
        return new_campaign
    except Exception as e:
        return None


def add_contacts_to_campaign_to_db(contact_rel_campaign, commit=True):
    try:
        db.session.add(contact_rel_campaign)
        if commit:
            db.session.commit( )
        return contact_rel_campaign
    except Exception as e:
        return None


def update_relation_campaign_to_db(campaign, commit=True):
    try:
        if commit:
            db.session.commit( )
        return campaign
    except Exception as e:
        return None


def get_campaign_by_id(id):
    return Campaign.query.get(id)


def get_crc_by_campaign_contact_id(campaign_id, contact_id):
    return ContactRelCampaign.query.filter_by(contact_id=contact_id, campaign_id=campaign_id)


def get_crc_by_campaign_id(id):
    return ContactRelCampaign.query.filter_by(campaign_id=id)


def set_crc_clicked_date(crc):
    crc.clicked_date = datetime.now()
    db.session.commit()

ALLOWED_EXTENSIONS = set(['txt'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower( ) in ALLOWED_EXTENSIONS


def url_generator(contact_id, campaign_id):
    return f'http://localhost:5000/campaign/{campaign_id}/contact/{contact_id}'
