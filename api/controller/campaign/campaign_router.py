import os

from flask import jsonify
from werkzeug.utils import secure_filename

from api.ProxySender.EmailSender import EmailSender
from api.controller import contact_blueprint
from api.controller.campaign.campaign_business import get_campaign_params_from_request, save_campaign_to_db, \
    get_file_param_from_request, allowed_file, get_campaign_by_id, get_campaign_contact_params_from_request, \
    add_contacts_to_campaign_to_db, get_publish_campaign_params_from_request, url_generator, get_crc_by_campaign_id, \
    get_crc_by_campaign_contact_id, set_crc_clicked_date
from api.controller.contact.contact_business import save_contact_to_db, commit_db, flush_db, get_contact_by_id, \
    calculate_duration
from api.models.Campaign import Campaign
from api.models.Contact import Contact
from api.models.CrcView import CrcView
from api.models.contact_rel_campaign import ContactRelCampaign
from api.parser.TextFileParser import TextFileParser
from api.schemas.CampaignSchema import campaign_schema
from api.utils.error_response import generate_error_response
from api.validators.CampaignValidator import validate_campaign


@contact_blueprint.route('/campaign', methods=['POST'])
def create_campaign():
    title, description = get_campaign_params_from_request()

    is_validation_succeed, err_msg = validate_campaign(title, description)
    if not is_validation_succeed:
        return generate_error_response(err_msg)

    new_campaign = save_campaign_to_db(Campaign(title, description))

    if not new_campaign:
        return generate_error_response("Error: An error occured")

    return campaign_schema.jsonify(new_campaign)


@contact_blueprint.route('/campaign/upload_contacts', methods=['POST'])
def upload_contacts_via_file():
    file = get_file_param_from_request()
    if file and allowed_file(file.filename):
        file_name = secure_filename(file.filename)
        file_path = os.path.join('uploads', file_name)
        file.save(file_path)
        tfp = TextFileParser(file_path)
        tfp.parse_file( )
        return jsonify(tfp.dictionary)
    else:
        return generate_error_response("Error: Upload file must be a text file")


@contact_blueprint.route('/campaign/<id>/add_contacts', methods=['POST'])
def add_contacts_to_campaign(id):
    campaign = get_campaign_by_id(id)
    contacts = get_campaign_contact_params_from_request()
    for c in contacts:
        new_contact = Contact(email=c['email'], full_name=c['full_name'])
        new_contact = save_contact_to_db(new_contact, False)
        flush_db()
        crc = ContactRelCampaign(id, new_contact.id)
        add_contacts_to_campaign_to_db(crc)
    commit_db()
    return campaign_schema.jsonify(campaign)


@contact_blueprint.route('/campaign/<id>/publish', methods=['POST'])
def publish_campaign(id):
    # campaign = get_campaign_by_id(id)
    body_text = get_publish_campaign_params_from_request()
    crc_list = get_crc_by_campaign_id(id)
    recvrs = []
    for crc in crc_list:
        body_text += ' ' + url_generator(crc.contact_id, id)
        contact = get_contact_by_id(id)
        recvrs.append(contact.email)

    es = EmailSender( )
    es.send(recvrs, crc, body_text)
    commit_db()
    return jsonify({'status': 'success'})


@contact_blueprint.route('/campaign/<id>/contact/<contact_id>', methods=['POST'])
def click_campaign_url(id, contact_id):
    crc = get_crc_by_campaign_contact_id(id, contact_id).one()
    set_crc_clicked_date(crc)
    return jsonify({'status': 'success'})


@contact_blueprint.route('/campaign/<id>/contacts', methods=['GET'])
def list_campaign_contacts(id):
    crc_list = get_crc_by_campaign_id(id)
    res_arr = []
    for crc in crc_list:
        contact = get_contact_by_id(crc.contact_id)
        crcv = CrcView()
        crcv.email = contact.email
        crcv.full_name = contact.full_name
        crcv.has_mail_sent = True if crc.sent_date else False
        crcv.has_receiver_clicked = True if crc.clicked_date else False
        if crcv.has_mail_sent and crcv.has_receiver_clicked:
            crcv.duration = calculate_duration(crc.sent_date, crc.clicked_date)
        res_arr.append(crcv.toJSON())

    return jsonify(res_arr)
