from api import ma


class ContactRelCampaignSchema(ma.Schema):
    class Meta:
        fields = ('id', 'campaign_id', 'contact_id', 'sent_date', 'clicked_date')


# Init schema
contact_rel_campaign_schema = ContactRelCampaignSchema( )
