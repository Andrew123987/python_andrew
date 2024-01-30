from fixture.app import App
import pytest

fixture = None
@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = App()
        fixture.session.login(username='admin',password='secret')
    else:
        if not fixture.is_valid():
            fixture = App()
            App.open_home_page()
    fixture.session.ensure_login("admin", "secret")
    return fixture

@pytest.fixture(scope='session', autouse=True)
def stop(request):


    def final():
        fixture.session.ensure_logout()
        fixture.stop()
    request.addfinalizer(final)
    return fixture