from api import ma


class ContactSchema(ma.Schema):
    class Meta:
        fields = ('id', 'full_name', 'email')


# Init schema
contact_schema = ContactSchema( )
contacts_schema = ContactSchema(many=True)
