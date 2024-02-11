from fixture.app import App
import pytest

fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption('--browser')
    base_url = request.config.getoption('--baseUrl')
    password = request.config.getoption('--password')
    username = request.config.getoption('--username')
    if fixture is None:

        fixture = App(browser=browser, base_url=base_url, password=password, username=username)
    else:
        if not fixture.is_valid():
            fixture = App(browser=browser, base_url=base_url, password=password, username=username)
            fixture.session.open_home_page()
    fixture.session.ensure_login(username, password)
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
    parser.addoption('--username', action='store')
    parser.addoption('--password', action='store')
