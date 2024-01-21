from fixture.app import App
import pytest

@pytest.fixture
def app(request):
    fixture = App()
    request.addfinalizer(fixture.stop)
    return fixture