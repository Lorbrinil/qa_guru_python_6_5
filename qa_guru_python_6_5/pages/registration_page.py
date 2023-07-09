from selene import browser, have
from models.users import User
from qa_guru_python_6_5 import resources


class RegistrationPage:
    def __init__(self):
        self.fill_first_name = browser.element('[id="firstName"]')
        self.fill_last_name = browser.element('[id="lastName"]')
        self.fill_user_email = browser.element('[id="userEmail"]')
        self.fill_user_number = browser.element('[id="userNumber"]')
        self.fill_hobby = browser.all('[for^=hobbies-checkbox]')
        self.fill_picture = browser.element('[type="file"]')
        self.fill_address = browser.element('[id="currentAddress"]')

    def register(self, user: User):
        self.fill_first_name.type(user.first_name)
        self.fill_last_name.type(user.last_name)
        self.fill_user_email.type(user.email)
        self.fill_gender(user.gender)
        self.fill_user_number.type(user.mobile_number)
        self.fill_date_of_birth(user.date_of_birth)
        self.fill_subject(user.subjects)
        self.fill_hobby.element_by(have.exact_text(user.hobbies.value)).click()
        self.fill_picture.send_keys(resources.path(user.image))
        self.fill_address.type(user.current_address)
        self.fill_state(user.state)
        self.fill_city(user.city)
        self.submit_form()
        return self


    def open(self):
        browser.open('/automation-practice-form')

    def fill_date_of_birth(self, date):
        year = date.year
        month = date.month - 1
        day = date.strftime('%d')
        browser.element('[id="dateOfBirthInput"]').click()
        browser.element('[class="react-datepicker__month-select"]').click()
        browser.element(f'[value="{month}"]').click()
        browser.element('[class="react-datepicker__year-select"]').click()
        browser.element(f'[value="{year}"]').click()
        browser.element(f'[class="react-datepicker__day react-datepicker__day--0{day}"]').click()
        return self

    def fill_gender(self, value):
        browser.element(f'[name=gender][value={value}]+label').click()
        return self

    def fill_subject(self, value):
        browser.element('[id="subjectsInput"]').type(value)
        browser.element('[id="react-select-2-option-0"]').click()
        return self

    def fill_state(self, value):
        browser.element('[id="state"]').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()
        return self

    def fill_city(self, value):
        browser.element('[id="city"]').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()
        return self

    def submit_form(self):
        browser.element('[id = "submit"]').click()

    def should_registrated_user_with(self, user):
        browser.element('[id = example-modal-sizes-title-lg]').should(have.text('Thanks for submitting the form'))
        browser.all('.table-responsive .table tbody > tr')[0].should(have.text(f'{user.first_name} {user.last_name}'))
        browser.all('.table-responsive .table tbody > tr')[1].should(have.text(f'{user.email}'))
        browser.all('.table-responsive .table tbody > tr')[2].should(have.text(f'{user.gender}'))
        browser.all('.table-responsive .table tbody > tr')[3].should(have.text(f'{user.mobile_number}'))
        browser.all('.table-responsive .table tbody > tr')[4].should(have.text(f'{user.date_of_birth.strftime("%d")} '
                                                                               f'{user.date_of_birth.strftime("%B")},'
                                                                               f'{user.date_of_birth.year}'))
        browser.all('.table-responsive .table tbody > tr')[5].should(have.text(f'{user.subjects}'))
        browser.all('.table-responsive .table tbody > tr')[6].should(have.text(f'{user.hobbies.value}'))
        browser.all('.table-responsive .table tbody > tr')[7].should(have.text(f'{user.image}'))
        browser.all('.table-responsive .table tbody > tr')[8].should(have.text(f'{user.current_address}'))
        browser.all('.table-responsive .table tbody > tr')[9].should(have.text(f'{user.state} {user.city}'))
