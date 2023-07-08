from qa_guru_python_6_5.pages.registration_page import RegistrationPage


def test_student_registration_form():

    registration_page = RegistrationPage()
    registration_page.open()

    (
    registration_page
        .fill_first_name('StudentName')
        .fill_last_name('StudentName2')
        .fill_user_email('name@ex.com')
        .fill_gender('Female')
        .fill_user_number('1234567890')
        .fill_date_of_birth('1996', '12', '12')
        .fill_subject('Physics')
        .fill_hobby('Sports')
        .fill_picture('icon.jpg')
        .fill_address('438 DARK SPURT SAN FRANCISCO CA 94528 USA')
        .fill_state('NCR')
        .fill_city('Delhi')
    )

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
