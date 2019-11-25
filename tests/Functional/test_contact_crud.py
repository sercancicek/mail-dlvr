import json
import uuid


def test_create_contact(test_client):
    """
       GIVEN a Flask application
       WHEN the '/contact' page is posted to (POST)
       THEN check the response is valid
       """
    mock_request_headers = {
        'Content-Type': 'application/json'
    }

    mock_request_data = {
            'full_name': 'Sercan Cicek',
            'email': f'{str(uuid.uuid4())}@sc.com'
    }
    response = test_client.post('/contact',
                                data=json.dumps(mock_request_data), headers=mock_request_headers)

    assert response.status_code == 200
    # assert response.data


