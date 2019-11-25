import io
import json
import uuid


def test_create_campaign(test_client):
    """
       GIVEN a Flask application
       WHEN the '/campaign' page is posted to (POST)
       THEN check the response is valid
       """
    mock_request_headers = {
        'Content-Type': 'application/json'
    }

    mock_request_data = {
        'title': f'Campaign {str(uuid.uuid4( ))[0: 20]}',
        'desc': 'Test campaign'
    }
    response = test_client.post('/campaign',
                                data=json.dumps(mock_request_data), headers=mock_request_headers)

    assert response.status_code == 200
    # assert response.data


def test_upload_contacts_to_campaign(test_client):
    """
       GIVEN a Flask application
       WHEN the '/campaign/contacts' page is posted to (POST)
       THEN check the response is valid
    """
    mock_request_headers = {
        'Content-Type': 'multipart/form-data'
    }

    data = {'name': 'this is a name', 'age': 12}
    data = {key: str(value) for key, value in data.items( )}

    data['file'] = (io.BytesIO(b'Edward Kmett <ekmett@example.com>\n' +
                               b'Simon Peyton Jones <spj@example.com>\n' +
                               b'Michael Snoyman <snoyberg@example.com>'), 'test.txt')

    response = test_client.post('/campaign/upload_contacts',
                                data=data, headers=mock_request_headers)

    assert response.status_code == 200
    # assert response.data


def test_add_contacts_to_campaign(test_client):
    """
       GIVEN a Flask application
       WHEN the '/campaign/contacts' page is posted to (POST)
       THEN check the response is valid
    """
    mock_request_headers = {
        'Content-Type': 'application/json'
    }

    mock_request_data = {
        'contacts': [
            {
                'id': 1,
                'email': f'{str(uuid.uuid4( ))[0: 5]}@aa.com',
                'full_name': 'John F. Kennedy'
            },
            {
                'id': 2,
                'email': f'{str(uuid.uuid4( ))[0: 5]}@aa.com',
                'full_name': 'John F. Kennedy'
            },
            {
                'id': 3,
                'email': f'{str(uuid.uuid4( ))[0: 5]}@aa.com',
                'full_name': 'John F. Kennedy'
            },
        ]
    }

    response = test_client.post('/campaign/1/add_contacts',
                                data=json.dumps(mock_request_data), headers=mock_request_headers)

    assert response.status_code == 200


def test_publish_campaign(test_client):
    """
       GIVEN a Flask application
       WHEN the '/campaign/contacts' page is posted to (POST)
       THEN check the response is valid
    """
    mock_request_headers = {
        'Content-Type': 'application/json'
    }

    mock_request_data = {
        'text': 'This email has been sent via by in out and through'
    }

    response = test_client.post('/campaign/1/publish',
                                data=json.dumps(mock_request_data), headers=mock_request_headers)

    assert response.status_code == 200


def test_click_url(test_client):
    """
       GIVEN a Flask application
       WHEN the '/campaign/contacts' page is posted to (POST)
       THEN check the response is valid
    """
    mock_request_headers = {
        'Content-Type': 'application/json'
    }

    mock_request_data = {
    }

    response = test_client.post('/campaign/1/contact/216',
                                data=json.dumps(mock_request_data), headers=mock_request_headers)

    assert response.status_code == 200


def test_list_campaign_contacts(test_client):
    """
       GIVEN a Flask application
       WHEN the '/campaign/contacts' page is posted to (POST)
       THEN check the response is valid
    """
    mock_request_headers = {
        'Content-Type': 'application/json'
    }

    mock_request_data = {
    }

    response = test_client.get('/campaign/1/contacts',
                                data=json.dumps(mock_request_data), headers=mock_request_headers)

    assert response.status_code == 200