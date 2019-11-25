from api.controller import contact_blueprint
from api.controller.contact.contact_business import save_contact_to_db, \
    get_params_from_request
from api.models.Contact import Contact
from api.schemas.ContactSchema import contact_schema
from api.utils.error_response import generate_error_response
from api.validators.ContactValidator import validate_contact


@contact_blueprint.route('/contact', methods=['POST'])
def create_contact():
    full_name, email = get_params_from_request()

    is_validation_succeed, err_msg = validate_contact(full_name, email)
    if not is_validation_succeed:
        return generate_error_response(err_msg)

    new_contact = Contact(full_name, email)
    new_contact = save_contact_to_db(new_contact)

    if not new_contact:
        return generate_error_response("Error: An error occured")

    return contact_schema.jsonify(new_contact)


