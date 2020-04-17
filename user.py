import pyperclip


class User:
    user_list = []

    def __init__(self, firstName, lastName, userName, password):

        self.firstName = firstName
        self.lastName = lastName
        self.userName = userName
        self.password = password

    def save_user(self):
        User.user_list.append(self)

    def delete_user(self):
        User.user_list.remove(self)

    @classmethod
    def find_user_by_name(cls, userName):
        for user in cls.user_list:
            if user.userName == userName:
                return userName

    @classmethod
    def user_exist(cls, userName):
        for user in cls.user_list:
            if user.userName == userName:
                return True

        return False

    @classmethod
    def display_user_name(cls):
        return cls.user_list

    @classmethod
    def copy_password(cls, password):
        user_found = User.find_by_password(password)
        pyperclip.copy(user_found.password)
