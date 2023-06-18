from selene import browser, have, command
import os


def test_student_registration_form():
    browser.open('/')

    browser.element('[id="firstName"]').type('StudentName')
    browser.element('[id="lastName"]').type('StudentName2')
    browser.element('[id="userEmail"]').type('name@ex.com')

    browser.element('[id="gender-radio-2"]').with_(click_by_js=True).click()

    browser.element('[id="userNumber"]').type('1234567890')

    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('[class="react-datepicker__month-select"]').click()
    browser.element('[value="11"]').click()
    browser.element('[class="react-datepicker__year-select"]').click()
    browser.element('[value="1996"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--012"]').click()

    browser.element('[id="subjectsInput"]').type('Ph')
    browser.element('[id="react-select-2-option-0"]').click()

    browser.element('[for="hobbies-checkbox-1"]').click()

    browser.element('[type="file"]').send_keys(os.path.abspath('resources/icon.jpg'))

    browser.element('[id="currentAddress"]').type('438 DARK SPURT SAN FRANCISCO CA 94528 USA')
    browser.element('[id="state"]').perform(command.js.scroll_into_view).click()
    browser.element('[id="react-select-3-option-0"]').click()
    browser.element('[id="city"]').click()
    browser.element('[id="react-select-4-option-0"]').click()

    browser.element('[id = "submit"]').click()

    browser.element('[id = example-modal-sizes-title-lg]').should(have.text('Thanks for submitting the form'))
    browser.all('.table-responsive .table tbody > tr')[0].should(have.text('StudentName StudentName2'))
    browser.all('.table-responsive .table tbody > tr')[1].should(have.text('name@ex.com'))
    browser.all('.table-responsive .table tbody > tr')[2].should(have.text('Female'))
    browser.all('.table-responsive .table tbody > tr')[3].should(have.text('1234567890'))
    browser.all('.table-responsive .table tbody > tr')[4].should(have.text('12 December,1996'))
    browser.all('.table-responsive .table tbody > tr')[5].should(have.text('Physics'))
    browser.all('.table-responsive .table tbody > tr')[6].should(have.text('Sports'))
    browser.all('.table-responsive .table tbody > tr')[7].should(have.text('icon.jpg'))
    browser.all('.table-responsive .table tbody > tr')[8].should(have.text('438 DARK SPURT SAN FRANCISCO CA 94528 USA'))
    browser.all('.table-responsive .table tbody > tr')[9].should(have.text('NCR Delhi'))
