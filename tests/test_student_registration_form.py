from pathlib import Path

from selene import browser
from selene.core.condition import Condition
from selene.support import by
from selene.support.conditions import have, be


def test_student_registration_form(set_browser):
    # Открытие сайта
    browser.open('/automation-practice-form')
    browser.element('h5').should(have.text('Student Registration Form'))

    # Заполнение данных
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
    # browser.element('#uploadPicture').send_keys(os.path.abspath('resources/Rattus.jpg'))
    file_path = str(Path('resources/Rattus.jpg').resolve())
    browser.element('#uploadPicture').send_keys(file_path)
    browser.element('#currentAddress').type('Some text for test')
    browser.element('#state').click()
    browser.element('#react-select-3-option-3').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-1').click()
    browser.element('#submit').click()

    # Проверка введенных данных
    browser.element(".modal-content").should(be.visible)
    browser.element(".modal-content").should((have.text("Thanks for submitting the form")))
    (browser.element(".table-responsive")
     .should(Condition.by_and(have.text("Student Name"), have.text("John Petrucci"))))
    (browser.element(".table-responsive")
     .should(Condition.by_and(have.text("Student Email"), have.text("god_of_bass@yahoo.com"))))
    (browser.element(".table-responsive")
     .should(Condition.by_and(have.text("Gender"), have.text("Male"))))
    (browser.element(".table-responsive")
     .should(Condition.by_and(have.text("Mobile"), have.text("9991125467"))))
    (browser.element(".table-responsive")
     .should(Condition.by_and(have.text("Date of Birth"), have.text("09 March,1990"))))
    (browser.element(".table-responsive")
     .should(Condition.by_and(have.text("Subjects"), have.text("Arts"))))
    (browser.element(".table-responsive")
     .should(Condition.by_and(have.text("Hobbies"), have.text("Music"))))
    (browser.element(".table-responsive")
     .should(Condition.by_and(have.text("Picture"), have.text("Rattus.jpg"))))
    (browser.element(".table-responsive")
     .should(Condition.by_and(have.text("Address"), have.text("Some text for test"))))
    (browser.element(".table-responsive")
     .should(Condition.by_and(have.text("State and City"), have.text("Rajasthan Jaiselmer"))))
