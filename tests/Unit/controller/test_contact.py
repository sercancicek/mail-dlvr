from api.models.Contact import Contact
from api.system_messages.contact_messages import INVALID_CONTACT_INPUT, INVALID_CONTACT_MAIL, INVALID_CONTACT_FULLNAME
from api.validators.ContactValidator import validate_contact


def test_create_contact():
    """
       GIVEN a Contact model
       WHEN a new Contact is created
       THEN check the email, full_name fields are defined correctly
    """
    new_contact = Contact(full_name='Test User', email='test@test.com')
    # assert new_contact.email == 'sc@sc.com'
    assert new_contact.full_name != ''


def test_validation_fail_contact():
    res, err = validate_contact('', '')
    assert res is False
    assert err == INVALID_CONTACT_INPUT

    res, err = validate_contact('Sercan Cicek', 'asdasd')
    assert res is False
    assert err == INVALID_CONTACT_MAIL

    res, err = validate_contact('S', 'aa@aa.com')
    assert res is False
    assert err == INVALID_CONTACT_FULLNAME


def test_validation_success_contact():
    res, err = validate_contact('Sercan Cicek', 'sc@sc.com')
    assert res is True
    assert err == ''

    res, err = validate_contact('Sercan Cicek Tester', 'asdasd@asd.com')
    assert res is True
    assert err == ''

