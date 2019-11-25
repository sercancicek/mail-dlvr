from api.controller.campaign.campaign_business import allowed_file
from api.models.Campaign import Campaign
from api.parser.TextFileParser import TextFileParser, parse_line
from api.system_messages.campaign_messages import *
from api.validators.CampaignValidator import validate_campaign


def test_create_campaign_without_users():
    """
       GIVEN a Campaign model
       WHEN a new Campaign is created
       THEN check the title, description fields are defined correctly
    """
    new_campaign = Campaign('My Test', 'Huge discount, 99% discounts have been started! Do not miss it')
    assert new_campaign.title == 'My Test'
    assert 'Huge discount' in new_campaign.description


def test_validation_fail_campaign():
    res, err = validate_campaign('', '')
    assert res is False
    assert err == INVALID_CAMPAIGN_INPUT

    res, err = validate_campaign('Title', 'd')
    assert res is False
    assert err == INVALID_CAMPAIGN_DESC

    res, err = validate_campaign('Title', 'd')
    assert res is False
    assert err == INVALID_CAMPAIGN_DESC

    res, err = validate_campaign('S', 'Description')
    assert res is False
    assert err == INVALID_CAMPAIGN_TITLE


def test_file_upload():
    tfp = TextFileParser('tests/source.txt')
    tfp.parse_file()
    assert len(tfp.dictionary) == 3


def test_parse_line():
    email, full_name = parse_line('Aaaa Bbb CCC <aa@aa.com>')
    assert email == 'aa@aa.com' and full_name == 'Aaaa Bbb CCC'

    email, full_name = parse_line('Aaaa Bbb CCC aaaa@aa.com>')
    assert email is None and full_name is None

    email, full_name = parse_line('Aaaa Bbb CCC <sercan>')
    assert email is None and full_name is None


def test_allowed_file():
    assert allowed_file('aaaa.txt') is True
    assert allowed_file('aaaa.png') is False
    assert allowed_file('aaaa') is False
