from api.system_messages.contact_messages import *
from api.validators.validation import validate_email_address


def validate_full_name(full_name):
    if len(full_name) < 2:
        return False
    elif len(full_name.split(' ')) < 2:
        return False

    return True


def validate_contact(full_name, email):
    if full_name == '' or email == '':
        return False, INVALID_CONTACT_INPUT
    elif not validate_email_address(email):
        return False, INVALID_CONTACT_MAIL
    elif not validate_full_name(full_name):
        return False, INVALID_CONTACT_FULLNAME

    return True, ''
