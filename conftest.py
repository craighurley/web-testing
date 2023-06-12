# content of conftest.py
import pytest


def pytest_addoption(parser):
    parser.addoption("--ns", action="store", default="", help="The name server to query.")


@pytest.fixture
def ns(request):
    return request.config.getoption("--ns")
