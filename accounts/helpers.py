import re
import phonenumbers


def validate_email(email):
    REGEX = '^(\w|.|_|-)+[@](\w|_|-|.)+[.]\w{2,3}$'
    if re.search(REGEX, email):
        return True
    return False


def validate_phone_number(phone_number, country_code):
    number = phonenumbers.parse(phone_number, country_code)
    return phonenumbers.is_valid_number(number)