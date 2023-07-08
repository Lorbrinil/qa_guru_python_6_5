from selene import browser, have

from qa_guru_python_6_5 import resources


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('[id="firstName"]').type(value)

    def fill_last_name(self, value):
        browser.element('[id="lastName"]').type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('[id="dateOfBirthInput"]').click()
        browser.element('[class="react-datepicker__month-select"]').click()
        browser.element(f'[value="{int(month)-1}"]').click()
        browser.element('[class="react-datepicker__year-select"]').click()
        browser.element(f'[value="{year}"]').click()
        browser.element(f'[class="react-datepicker__day react-datepicker__day--0{day}"]').click()

    def fill_user_email(self, value):
        browser.element('[id="userEmail"]').type(value)

    def fill_gender(self, value):
        browser.element(f'[name=gender][value={value}]+label').click()

    def fill_user_number(self, value):
        browser.element('[id="userNumber"]').type(value)

    def fill_subject(self, value):
        browser.element('[id="subjectsInput"]').type(value)
        browser.element('[id="react-select-2-option-0"]').click()

    def fill_hobby(self, value):
        browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text(value)).click()

    def fill_picture(self, value):
        browser.element('[type="file"]').send_keys(resources.path(value))

    def fill_address(self, value):
        browser.element('[id="currentAddress"]').type(value)

    def fill_state(self, value):
        browser.element('[id="state"]').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()

    def fill_city(self, value):
        browser.element('[id="city"]').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()

    def submit_form(self):
        browser.element('[id = "submit"]').click()

    def should_registrated_user_with(self, student_name, email, gender, mobile, date_of_birth, subjects, hobbies,
                                     picture, address, state_and_city):
        browser.element('[id = example-modal-sizes-title-lg]').should(have.text('Thanks for submitting the form'))
        browser.all('.table-responsive .table tbody > tr')[0].should(have.text(student_name))
        browser.all('.table-responsive .table tbody > tr')[1].should(have.text(email))
        browser.all('.table-responsive .table tbody > tr')[2].should(have.text(gender))
        browser.all('.table-responsive .table tbody > tr')[3].should(have.text(mobile))
        browser.all('.table-responsive .table tbody > tr')[4].should(have.text(date_of_birth))
        browser.all('.table-responsive .table tbody > tr')[5].should(have.text(subjects))
        browser.all('.table-responsive .table tbody > tr')[6].should(have.text(hobbies))
        browser.all('.table-responsive .table tbody > tr')[7].should(have.text(picture))
        browser.all('.table-responsive .table tbody > tr')[8].should(have.text(address))
        browser.all('.table-responsive .table tbody > tr')[9].should(have.text(state_and_city))
