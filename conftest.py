from fixture.app import App
import pytest
import json
import os.path

fixture = None
target = None

@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption('--browser')
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption('--target'))
        with open(config_file) as f:
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = App(browser=browser, base_url=target['base_url'], username=target['username'], password=target['password'])
    fixture.session.ensure_login(username=target['username'], password=target['password'])
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
    parser.addoption('--target', action='store', default='target.json')

