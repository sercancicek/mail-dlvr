from datetime import datetime

from flask import request

from api import db
from api.models.Contact import Contact
from dateutil.relativedelta import relativedelta


def get_params_from_request():
    return request.json['full_name'], request.json['email']


def save_contact_to_db(new_contact, commit=True):
    try:
        db.session.add(new_contact)
        if commit:
            db.session.commit( )
        return new_contact
    except Exception as e:
        return None


def get_contact_by_id(id):
    return Contact.query.get(id)


def flush_db():
    try:
        db.session.flush( )
    except Exception as e:
        return None


def commit_db():
    try:
        db.session.commit( )
    except Exception as e:
        return None


def calculate_duration(sent_date, clicked_date):
    diff = relativedelta(sent_date, clicked_date)
    return "%d year %d month %d days %d hours %d minutes %dseconds" % (
        diff.years, diff.months, diff.days, diff.hours, diff.minutes, diff.seconds)
