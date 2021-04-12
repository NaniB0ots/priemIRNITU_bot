import re

from django.core.exceptions import ValidationError


def phone_number_validation(phone_number: str):
    rule = re.compile('^((8|\+7)[\- ]?)?(\(?\d{3,4}\)?[\- ]?)?[\d\- ]{5,10}$')
    if not rule.search(phone_number):
        msg = u"Invalid mobile number."
        raise ValidationError(msg)


def is_valid_phone_number(phone_number: str) -> bool:
    try:
        phone_number_validation(phone_number)
        return True
    except ValidationError:
        return False
