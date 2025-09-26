#1. Implement a `PasswordManager` class where the password is private (`__password`). Add methods to set and validate the password.

import string

class PasswordManager:

    def __init__(self, password):
        self.__password = password

    def validate_password(self, password=None):
        if password is None:
            password = self.__password
        has_lower = any(ch in string.ascii_lowercase for ch in password)
        has_upper = any(ch in string.ascii_uppercase for ch in password)
        has_digit = any(ch in string.digits for ch in password)
        has_special = any(ch in string.punctuation for ch in password)

        return all([has_lower, has_upper, has_digit, has_special])


    # Setter method
    def set_password(self, password):
        if self.validate_password(password):
            self.__password = password
            return "Password Updated Succesfully!"
        else:
            return "Password must contain uppercase, lowercase, digits and special character."

p1 = PasswordManager("GopalMahato@2026")
print(p1.validate_password())
