# Sourced From https://flask.palletsprojects.com/en/2.0.x/testing/
import pytest
from app import app

@pytest.fixture
def theapp():
    theapp = app()
    theapp.config.update({
        "TESTING": True,
    })

    yield theapp

@pytest.fixture()
def client(theapp):
    return theapp.test_client()


@pytest.fixture()
def runner(theapp):
    return theapp.test_cli_runner()