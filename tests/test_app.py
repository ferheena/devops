# ensure contains the following:
import sys
sys.path.append('/opt/dd/devops/app')
import pytest
from app import *
    
@pytest.fixture
def client():
    client = app.test_client()
    return client
    
def test_root(client):
    """Test the default route."""
   
    res = client.get('/')
    assert b'Hello world!' in res.data
