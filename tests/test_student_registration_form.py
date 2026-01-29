import pytest
from selene import browser
from selene.support.conditions import have


@pytest.fixture(scope='function')
def set_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    #browser.close()

def test_student_registration_form(set_browser):
    browser.open('/automation-practice-form')
    browser.element('h5').should(have.text('Student Registration Form'))