import datetime

from api.Observer.Observer import Observer
from api.controller.campaign.campaign_business import update_relation_campaign_to_db
from api.controller.contact.contact_business import flush_db


class MailEvents(Observer):
    def update(self, crc, clicked_date=''):
        if crc and clicked_date:
            crc.clicked_date = clicked_date
        else:
            crc.sent_date = datetime.datetime.now()

        update_relation_campaign_to_db(crc, False)
        flush_db()
