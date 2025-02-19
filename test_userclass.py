from datetime import datetime

from usercl import User
from user_service import UserService
from user_util import UserUtil

if __name__ == "__main__":
    user1 = User(1, 'John', 'Doe', '2000-10-06', 'john.doe@example.com')
    user2 = User(2, 'Jane', 'Smith', '1995-05-20', 'jane.smith@example.com')

    UserService.add_user(user1)
    UserService.add_user(user2)

    user1.password = UserUtil.generate_password()
    user2.password = UserUtil.generate_password()

    print(f"User1 Password: {user1.password}")
    print(f"User2 Password: {user2.password}")

    for person in UserService.users.values():
        print(person.get_details())
        print(f"User's password is strong: {UserUtil.is_strong_password(person.password)}")

    print(user1.user_id)
