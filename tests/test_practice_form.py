from qa_guru_python_6_5.pages.registration_page import RegistrationPage
import datetime
from models.users import User
from models.users import Hobby
import allure


@allure.title('Successful fill registration form')
def test_student_registration_form():

    registration_page = RegistrationPage()
    student = User(
        first_name='StudentName',
        last_name='StudentName2',
        email='name@ex.com',
        gender='Female',
        mobile_number='1234567890',
        subjects='Physics',
        date_of_birth=datetime.date(1996, 12, 12),
        hobbies=Hobby.reading,
        image='icon.jpg',
        current_address='438 DARK SPURT SAN FRANCISCO CA 94528 USA',
        state='NCR',
        city='Delhi'
    )

    with allure.step('Open registration form'):
        registration_page.open()

    with allure.step('Fill registration form'):
        registration_page.register(student)

    with allure.step('Check results'):
        registration_page.should_registrated_user_with(student)
