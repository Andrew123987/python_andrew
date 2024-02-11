from fixture.app import App
import pytest

fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        browser = request.config.getoption('--browser')
        base_url = request.config.getoption('--baseUrl')
        fixture = App(browser=browser, base_url=base_url)
        ##fixture.session.login(username='admin', password='secret')
    else:
        if not fixture.is_valid():
            fixture = App()
            fixture.session.open_home_page()
    fixture.session.ensure_login("admin", "secret")
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def final():
        fixture.session.ensure_logout()
        fixture.stop()
    request.addfinalizer(final)
    return fixture


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--baseUrl', action='store', default='http://localhost/addressbook/addressbook/')
