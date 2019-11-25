from flask import Blueprint
contact_blueprint = Blueprint('contact', __name__, template_folder='templates')

from api.controller.contact import contact_router
from api.controller.campaign import campaign_router
