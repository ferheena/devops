import sys
sys.path.append('/opt/hello_world/app')
import pytest
from app import *

@pytest.fixture
def client():
    client = app.test_client()
    #client = 'Hello world!'
    return client

def test_root(client):
    """Test the default route."""

    res = client.get('/')
    print res
    print res.data
    assert b'Hello world!' in res.data
