import os

from selene import browser
from selene.support import by
from selene.support.conditions import have

def test_student_registration_form(set_browser):
    browser.open('/automation-practice-form')
    browser.element('h5').with_(timeout=15).should(have.text('Student Registration Form'))
    browser.element('#firstName').type('John')
    browser.element('#lastName').type('Petrucci')
    browser.element('#userEmail').type('god_of_bass@yahoo.com')
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').type('9991125467')
    browser.element("#dateOfBirthInput").click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').element(by.text('1990')).click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select').element(by.text('March')).click()
    browser.element('.react-datepicker__day--009:not(react-datepicker__day--outside-month)').click()
    browser.element('#subjectsInput').type('Arts').press_enter()
    browser.element('#hobbiesWrapper').element(by.text("Music")).click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/Rattus.jpg'))