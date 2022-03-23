import pytest
from seva_zaika_sdk import LotrApi


@pytest.fixture
def client():
    return LotrApi(api_key="7DdfgMYZxv2bgKRY3mB4")
