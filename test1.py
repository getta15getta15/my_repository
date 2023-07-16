import requests
import pytest

def test_itswork():
    my_rqst = requests.get("https://dog.ceo/dog-api/")
    assert my_rqst.status_code == 200

def test_random():
    my_rqst = requests.get("https://dog.ceo/api/breeds/image/random")
    assert my_rqst.json()["status"] == "success"

@pytest.mark.parametrize("count", [3])
def test_random_image_by_size(count):
    my_rqst = requests.get(f"https://dog.ceo/api/breed/husky/images/random/{count}")
    assert len(my_rqst.json()['message']) == count
    
@pytest.mark.parametrize("animals, status_code", [("cat", 404)])
def test_cat_notfind(animals, status_code):
    my_rqst = requests.get(f"https://dog.ceo/api/breed/{animals}/images/random")
    assert my_rqst.status_code == status_code        

def test_jpg():
    my_rqst = requests.get("https://dog.ceo/api/breeds/image/random")
    assert my_rqst.json()["message"].find("jpg") != -1

