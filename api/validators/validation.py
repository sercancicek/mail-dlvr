import re

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


def validate_email_address(email):
    if re.search(regex, email):
        return True

    return False
