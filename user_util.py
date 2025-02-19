from datetime import datetime
from random import randint
from user_service import UserService
import random, string


class UserUtil:
    @staticmethod
    def generate_user_id():
        year = str(datetime.now().year)
        num = f"{randint(1, 9999999):07d}"
        user_id = year[2:] + num
        if user_id in UserService.users.keys():
            num = f"{randint(1, 9999999):07d}"
            user_id = year[2:] + num
            return user_id
        else:
            return user_id

    @staticmethod
    def generate_password(length=8):
        if length < 8:
            raise ValueError("Length of password must be at least 8")

        password = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(string.punctuation)]

        all_chars = string.ascii_letters + string.digits + string.punctuation
        password += (random.choices(all_chars, k=length - 4))
        random.shuffle(password)
        password = ''.join(password)
        return password

    @staticmethod
    def is_strong_password(password):
        uppercase = False
        lowercase = False
        number = False
        special_char = False

        for char in password:
            if char in string.ascii_uppercase:
                uppercase = True
            elif char in string.ascii_lowercase:
                lowercase = True
            elif char in string.digits:
                number = True
            elif char in string.punctuation:
                special_char = True

        return uppercase and lowercase and number and special_char

    @staticmethod
    def generate_email(name, surname, domain='gmail.com'):
        return f"{name.lower().replace(' ', '_')}.{surname.lower().replace(' ', '_')}@{domain}"

    @staticmethod
    def validate_email(email):
        if email.count('@') != 1:
            return False
        email_components = email.split('@')

        if '.' not in email_components[0]:
            return False

        if '.' not in email_components[1]:
            return False

        part1 = email_components[0].split('.')
        part2 = email_components[1].split('.')

        if not part1[0].isalpha() or not part1[1].isalpha():
            return False

        if len(part2) < 2:
            return False

        if part2[-1] != 'com':
            return False

        return True





