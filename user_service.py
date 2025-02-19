from usercl import User


class UserService:
    users = {}

    @classmethod
    def add_user(cls, user: User):
        user_id = user.user_id
        cls.users[user_id] = user

    @classmethod
    def find_user(cls, user_id):
        return cls.users[user_id]

    @classmethod
    def delete_user(cls, user_id):
        del cls.users[user_id]

    @classmethod
    def update_user(cls, user_id, user_update:User):
        cls.users[user_id] = user_update

    @classmethod
    def get_number(cls):
        return len(cls.users)

    @classmethod
    def get_all_users(cls):
        return list(cls.users.values())