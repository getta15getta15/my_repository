import requests
import pytest

def test_4(get_url, get_status):
    my_rqst = requests.get(get_url)
    assert my_rqst.status_code == int(get_status)

