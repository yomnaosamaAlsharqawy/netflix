import phonenumbers


def validate_phone_number(phone_number, country_code):
    number = phonenumbers.parse(phone_number, country_code)
    return phonenumbers.is_valid_number(number)