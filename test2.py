import requests
import pytest

@pytest.mark.parametrize("url", ["https://www.openbrewerydb.org/"])
def test_itswork(url):
    my_rqst = requests.get(f'{url}')
    assert my_rqst.status_code == 200

@pytest.mark.parametrize("url_paaram", ["not_find_data"])
def test_not_find_data(url_paaram):
    my_rqst = requests.get("https://api.openbrewerydb.org/v1/breweries/autocomplete?query={url_paaram}")
    assert my_rqst.status_code == 200 and len(my_rqst.json()) == 0

def test_sub_reqst():
    my_rqst = requests.get("https://api.openbrewerydb.org/v1/breweries/random")
    my_rqst = requests.get(f'https://api.openbrewerydb.org/v1/breweries/' + my_rqst.json()[0]['id'])
    if my_rqst.status_code == 200:
        my_rqst = requests.get(f'https://api.openbrewerydb.org/v1/breweries/' + my_rqst.json()[0]['id'])
        assert len(my_rqst.json()) != 0
    else:
        assert False

@pytest.mark.parametrize("url, status_code", [("https://www.openbrewerydb.org/errrrrrror", 404)])
def test_error_url(url, status_code):
    my_rqst = requests.get(f'{url}')
    assert my_rqst.status_code == status_code  

@pytest.mark.parametrize("per_page", [(4)])
def test_cat_notfind(per_page):
    my_rqst = requests.get(f'https://api.openbrewerydb.org/v1/breweries?per_page={per_page}')
    assert len(my_rqst.json()) == per_page
    
