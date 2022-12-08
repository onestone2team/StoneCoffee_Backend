import re

#profile name 이름에 _뺀 나머지 특수문자만 허용
def profile_name_validator(profilename):
    is_profilename = re.compile(r'^[a-zA-Z0-9+_]{4,}')
    if is_profilename.fullmatch(profilename) == None:
        return False
    return True



def email_validator(email):
    is_email = re.compile(r'^[a-zA-Z0-9+-_.]+@([a-zA-Z0-9-]{4,})+\.[a-zA-Z0-9-.]+$')
    if not is_email.fullmatch(email):
        return False
    return True


def password_check_validator(password, password_check):
    if password == '':
        return False
    else:
        if password != password_check:
            return False
        else:
            return True

def password_vaildator(phone, phone2):
    is_password = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@!%*#?&])[A-Za-z\d@!%*#?&]{8,}$')
    if not is_password.fullmatch(phone) or not is_password.fullmatch(phone2):
        return False
    return True

def phone_validator(phone):
    is_phone = re.compile(r'\d{3}-\d{3,4}-\d{4}')
    if not is_phone.fullmatch(phone):
        return False
    return True

def address_validator(address):
    is_address = re.compile(r"^[가-힣A-Za-z·\d~\-\.]{2,}")
    if not is_address.fullmatch(address):
        return False
    return True


