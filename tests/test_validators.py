from lib.utils.validators import is_valid_email

def test_is_valid_email():
    valid_email = 'foobar@gmail.com'
    invalid_email = 'foobar'

    check_for_valid_email = is_valid_email(valid_email)
    check_for_invalid_email = is_valid_email(invalid_email)

    assert check_for_valid_email == True
    assert check_for_invalid_email == False

