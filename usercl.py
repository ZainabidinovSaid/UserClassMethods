from datetime import date


class User:
    def __init__(self,user_id, name, surname, birthday = None, email = '', password = ''):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.birthday = birthday

    def get_details(self):
        return f"User ID: {self.user_id}, Name: {self.name} {self.surname}, Email: {self.email}, Birthday: {self.birthday}"
    def get_age(self):
        today = date.today().year
        return today-self.birthday.year