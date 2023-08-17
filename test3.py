import requests
import pytest

@pytest.mark.parametrize("url", ["https://jsonplaceholder.typicode.com/"])
def test_itswork(url):
    my_rqst = requests.get(f'{url}')
    assert my_rqst.status_code == 200

@pytest.mark.parametrize("url", ["https://jsonplaceholder.typicode.com/posts/"])
@pytest.mark.parametrize("post", ["1"])
def test_get_post(url, post):
    my_rqst = requests.get(f'{url}{post}')
    assert my_rqst.status_code == 200 and str(my_rqst.json()["id"]) == post

@pytest.mark.parametrize("url", ["https://jsonplaceholder.typicode.com/comments?postId="])
@pytest.mark.parametrize("post", ["1"])    
def test_get_comment(url, post):
    my_rqst = requests.get(f'{url}{post}')
    assert my_rqst.status_code == 200 and len(my_rqst.json()) != 0

@pytest.mark.parametrize("url", ["https://jsonplaceholder.typicode.com/posts?userId="])
@pytest.mark.parametrize("user", ["1"])    
def test_get_by_user(url, user):
    my_rqst = requests.get(f'{url}{user}')
    assert my_rqst.status_code == 200 and len(my_rqst.json()) != 0

@pytest.mark.parametrize("url", ["https://jsonplaceholder.typicode.com/posts"])
@pytest.mark.parametrize("param", ["{'title': 'foo','body': 'bar','userId': '938'}"])    
def test_create_post(url, param):
    my_rqst = requests.post(url, data=param)
    assert my_rqst.status_code == 200 and len(my_rqst.json()) != 0
