from qa_guru_python_6_5.pages.registration_page import RegistrationPage


def test_student_registration_form():

    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.fill_first_name('StudentName')
    registration_page.fill_last_name('StudentName2')
    registration_page.fill_user_email('name@ex.com')
    registration_page.fill_gender('Female')
    registration_page.fill_user_number('1234567890')
    registration_page.fill_date_of_birth('1996', '12', '12')
    registration_page.fill_subject('Physics')
    registration_page.fill_hobby('Sports')
    registration_page.fill_picture('icon.jpg')
    registration_page.fill_address('438 DARK SPURT SAN FRANCISCO CA 94528 USA')
    registration_page.fill_state('NCR')
    registration_page.fill_city('Delhi')

    registration_page.submit_form()

    registration_page.should_registrated_user_with(
        'StudentName StudentName2',
        'name@ex.com',
        'Female',
        '1234567890',
        '12 December,1996',
        'Physics',
        'Sports',
        'icon.jpg',
        '438 DARK SPURT SAN FRANCISCO CA 94528 USA',
        'NCR Delhi'
    )
