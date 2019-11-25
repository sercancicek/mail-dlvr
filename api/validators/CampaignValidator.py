from api.system_messages.campaign_messages import *


def validate_description(desc):
    if len(desc) < 2 or len(desc) > 500:
        return False

    return True


def validate_title(title):
    if len(title) < 2 or len(title) > 50:
        return False

    return True


def validate_campaign(title, desc):
    if title == '' or desc == '':
        return False, INVALID_CAMPAIGN_INPUT
    elif not validate_description(desc):
        return False, INVALID_CAMPAIGN_DESC
    elif not validate_title(title):
        return False, INVALID_CAMPAIGN_TITLE

    return True, ''
