from api import create_app
from logging import FileHandler, WARNING

from api.Events.MailEvents import MailEvents
from api.ProxySender.EmailSender import EmailSender

app = create_app('prod.cfg')

file_handler = FileHandler('picus_log.txt')
file_handler.setLevel(WARNING)

app.logger.addHandler(file_handler)

me = MailEvents()
ems = EmailSender()
ems.attach(me)

#
# class ContactRelCampaign(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     campaign_id = db.Column(db.Integer)
#     contact_id = db.Column(db.Integer)
#     sent_date = db.Column(db.DateTime)
#     clicked_date = db.Column(db.DateTime)
#
#
# class ContactRelCampaignSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'campaign_id', 'contact_id', 'sent_date', 'clicked_date')
#
#
# # Init schema
# contact_rel_campaign_schema = ContactRelCampaignSchema( )
#
#
# # Create a Contact
#
#
#
# # get all contacts
# @app.route('/contact', methods=['GET'])
# def get_contacts():
#     all_contacts = Contact.query.all( )
#     result = contacts_schema.dump(all_contacts)
#     return jsonify(result)
#
#
# @app.route('/contact/<id>', methods=['GET'])
# def get_contact(id):
#     contact = Contact.query.get(id)
#     return contact_schema.jsonify(contact)
#
#
# # Update a Contact
# @app.route('/contact/<id>', methods=['PUT'])
# def update_contact(id):
#     contact = Contact.query.get(id)
#
#     contact.full_name = request.json['full_name']
#     contact.email = request.json['email']
#
#     db.session.commit( )
#
#     return contact_schema.jsonify(contact)
#
# # Delete Contact
# @app.route('/contact/<id>', methods=['DELETE'])
# def delete_contact(id):
#     contact = Contact.query.get(id)
#     db.session.delete(contact)
#     db.session.commit()
#     return contact_schema.jsonify(contact)
#

# run server
if __name__ == '__main__':
    app.run(debug=True)
