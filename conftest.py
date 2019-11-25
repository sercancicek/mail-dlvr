import pytest

from api import create_app, db
from api.Events.MailEvents import MailEvents
from api.ProxySender.EmailSender import EmailSender
from api.models.Contact import Contact


@pytest.fixture(scope='module')
def new_contact():
    contact = Contact('Sercan Cicek', 'sc@sc.com')
    return contact


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('test.cfg')
    testing_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()
    me = MailEvents( )
    ems = EmailSender( )
    ems.attach(me)
    yield testing_client  # this is where the testing happens!

    ctx.pop()


@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table
    db.create_all( )

    # Insert user data
    contact = Contact(email='patkennedy79@gmail.com', full_name='Pat Kennedy')
    contact2 = Contact(email='kennedyfamilyrecipes@gmail.com', full_name='Kennedy Family')
    db.session.add(contact)
    db.session.add(contact2)

    # Commit the changes for the users
    db.session.commit( )

    yield db  # this is where the testing happens!

    db.drop_all()
