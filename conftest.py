import pytest

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='Chrome')
    parser.addoption('--url', action='store', default='https://www.opencart.com/')

@pytest.fixture
def get_browser(request):
    return request.config.getoption("--browser")

@pytest.fixture
def get_url(request):
    return request.config.getoption("--url")
