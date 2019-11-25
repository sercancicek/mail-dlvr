from api import ma


class CampaignSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description')


campaign_schema = CampaignSchema( )
campaigns_schema = CampaignSchema(many=True)
