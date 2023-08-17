import pytest

def pytest_addoption(parser):
    parser.addoption('--url', action='store', default='https://ya.ru')
    parser.addoption('--status_code', action='store', default=200)

@pytest.fixture
def get_url(request):
    return request.config.getoption("--url")

@pytest.fixture
def get_status(request):
    return request.config.getoption("--status_code")

