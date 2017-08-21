import os
import sys

import pytest

from datetime import datetime

from pyvirtualdisplay import Display
from selenium import webdriver


_IMPLICIT_WAIT = 20
SCREEN_RESOLUTION = (1600, 900)

env = os.getenv('TRAVIS', None)

if env:
    display = Display(visible=0, size=SCREEN_RESOLUTION)
    display.start()


def chrome_options():
    co = webdriver.ChromeOptions()
    co.add_argument('--headless')
    return co


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        choices=('firefox', 'chrome', 'edge', 'ie', 'no'),
        help='Select your desired browser.'
    )


@pytest.fixture(scope='function',
                params=[
                    pytest.param('edge',
                                 marks=pytest.mark.skipif(
                                     sys.platform != 'win32',
                                     reason="Only on Windows"),
                                 ),
                    pytest.param('ie',
                                 marks=pytest.mark.skipif(
                                     sys.platform != 'win32',
                                     reason="Only on Windows")
                                 ),
                    'firefox',
                    'chrome']
                )
def driver(request):
    """ This creates a selenium browser instance """
    browser = request.param
    try:
        if browser == 'no':
            return
        elif browser == 'firefox':
            driver = webdriver.Firefox()
        elif browser == 'chrome':
            driver = webdriver.Chrome(chrome_options=chrome_options())
        elif browser == 'edge':
            driver = webdriver.Edge()
        elif browser == 'ie':
            driver = webdriver.Ie()

    except KeyError:
        raise Exception('Selenium Driver not found')

    driver.implicitly_wait(_IMPLICIT_WAIT)

    driver.set_window_size(*SCREEN_RESOLUTION)
    request.addfinalizer(driver.quit)
    yield driver


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    summary = []
    extra = getattr(report, 'extra', [])
    driver = getattr(item, '_driver', None)
    xfail = hasattr(report, 'wasxfail')
    failure = (report.skipped and xfail) or (report.failed and not xfail)
    when = item.config.getini('selenium_capture_debug').lower()
    capture_debug = when == 'always' or (when == 'failure' and failure)
    if driver is not None:
        if capture_debug:
            exclude = item.config.getini('selenium_exclude_debug')
            if 'url' not in exclude:
                _gather_url(item, report, driver, summary, extra)
            if 'screenshot' not in exclude:
                _gather_screenshot(item, report, driver, summary, extra)
            if 'html' not in exclude:
                _gather_html(item, report, driver, summary, extra)
            if 'logs' not in exclude:
                _gather_logs(item, report, driver, summary, extra)
        driver_name = item.config.option.driver
    if summary:
        report.sections.append(('Selenium', '\n'.join(summary)))
    report.extra = extra


def _gather_url(item, report, driver, summary, extra):
    try:
        url = driver.current_url
    except Exception as e:
        summary.append('WARNING: Failed to gather URL: {0}'.format(e))
        return
    pytest_html = item.config.pluginmanager.getplugin('html')
    if pytest_html is not None:
        # add url to the html report
        extra.append(pytest_html.extras.url(url))
    summary.append('URL: {0}'.format(url))


def _gather_screenshot(item, report, driver, summary, extra):
    try:
        screenshot = driver.get_screenshot_as_base64()
    except Exception as e:
        summary.append('WARNING: Failed to gather screenshot: {0}'.format(e))
        return
    pytest_html = item.config.pluginmanager.getplugin('html')
    if pytest_html is not None:
        # add screenshot to the html report
        extra.append(pytest_html.extras.image(screenshot, 'Screenshot'))


def _gather_html(item, report, driver, summary, extra):
    try:
        html = driver.page_source.encode('utf-8')
    except Exception as e:
        summary.append('WARNING: Failed to gather HTML: {0}'.format(e))
        return
    pytest_html = item.config.pluginmanager.getplugin('html')
    if pytest_html is not None:
        # add page source to the html report
        extra.append(pytest_html.extras.text(html, 'HTML'))


def _gather_logs(item, report, driver, summary, extra):
    try:
        types = driver.log_types
    except Exception as e:
        # note that some drivers may not implement log types
        summary.append('WARNING: Failed to gather log types: {0}'.format(e))
        return
    for name in types:
        try:
            log = driver.get_log(name)
        except Exception as e:
            summary.append('WARNING: Failed to gather {0} log: {1}'.format(
                name, e))
            return
        pytest_html = item.config.pluginmanager.getplugin('html')
        if pytest_html is not None:
            extra.append(pytest_html.extras.text(
                format_log(log), '%s Log' % name.title()))


def _gather_cloud_url(provider, item, report, driver, summary, extra):
    try:
        url = provider.url(item.config, driver.session_id)
    except Exception as e:
        summary.append('WARNING: Failed to gather {0} job URL: {1}'.format(
            provider.name, e))
        return
    summary.append('{0} Job: {1}'.format(
        provider.name, url))
    pytest_html = item.config.pluginmanager.getplugin('html')
    if pytest_html is not None:
        # always add cloud job url to the html report
        extra.append(pytest_html.extras.url(
            url, '{0} Job'.format(provider.name)))


def _gather_cloud_extras(provider, item, report, driver, summary, extra):
    try:
        extras = provider.additional_html(driver.session_id)
    except Exception as e:
        summary.append('WARNING: Failed to gather {0} extras: {1}'.format(
            provider.name, e))
        return
    pytest_html = item.config.pluginmanager.getplugin('html')
    if pytest_html is not None:
        extra.append(pytest_html.extras.html(extras))


def _update_cloud_status(provider, item, report, driver, summary):
    xfail = hasattr(report, 'wasxfail')
    passed = report.passed or (report.failed and xfail)
    try:
        provider.update_status(item.config, driver.session_id, passed)
    except Exception as e:
        summary.append('WARNING: Failed to update {0} status: {0}'.format(
            provider.name, e))


def format_log(log):
    timestamp_format = '%Y-%m-%d %H:%M:%S.%f'
    entries = [u'{0} {1[level]} - {1[message]}'.format(
        datetime.utcfromtimestamp(entry['timestamp'] / 1000.0).strftime(
            timestamp_format), entry).rstrip() for entry in log]
    return '\n'.join(entries).encode('utf-8')
