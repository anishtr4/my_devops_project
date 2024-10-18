import pytest
from app import app, db
from config import TestConfig

@pytest.fixture(scope='module')
def test_client():
    app.config.from_object(TestConfig)
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='function')
def init_database(test_client):
    db.create_all()
    yield
    db.session.remove()
    db.drop_all()