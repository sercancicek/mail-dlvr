def test_new_contact(new_contact):
    """
       GIVEN a Contact model
       WHEN a new Contact is created
       THEN check the email, full_name fields are defined correctly
    """
    assert new_contact.email == 'sc@sc.com'
    assert new_contact.full_name != ''
