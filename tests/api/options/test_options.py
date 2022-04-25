import pytest
import requests


@pytest.fixture
def url(request):
    return request.config.getoption('--url')


@pytest.fixture
def status_code(request):
    return request.config.getoption('--status_code')


def test_response_status(url, status_code):
    assert requests.get(url).status_code == int(status_code)
