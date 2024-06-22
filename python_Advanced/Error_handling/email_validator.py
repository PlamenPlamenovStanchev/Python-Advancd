class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


EMAIL_MINIMAL_LENGTH = 5
VALID_DOMAIN_NAMES = ['com', 'bg', 'org', 'net']

while True:
    email = input()
    if email == 'End':
        break

    if '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')

    if len(email.split('@')[0]) < EMAIL_MINIMAL_LENGTH:
        raise NameTooShortError('Name must be more than 4 characters')

    domain = email.split('.')[-1]
    if f'{domain}' not in VALID_DOMAIN_NAMES:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    print('Email is valid')
