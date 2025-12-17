from utilities.utils import clear_console
from managers.input_manager import InputManager
from managers.user_manager import UserManager


class UserRegistration:
    def show(self):
        while True:
            clear_console()
            print("=== USER PROFILE ===")
            print('\nAt any point, input "n" to cancel.')

            while True:
                first_name = input('\nFirst Name: ').strip()
                if first_name.lower() == 'n':
                    return 'main'
                last_name = input('\nLast Name: ').strip()
                if last_name.lower() == 'n':
                    return 'main'
                validate_names = InputManager.validate_name(
                    first_name, last_name)
                if validate_names is False:
                    print('Only valid characters allowed...')
                    continue
                if validate_names is True:
                    break

            while True:  # needs length check cant be empty
                username = input('\nUsername: ')
                if username.lower() == 'n':
                    return 'main'
                result = UserManager.username_exists(username=username)
                if result is True:  # does exist is True
                    print(f'Username: {username} is already taken.')
                    continue
                break

            while True:  # Needs checks for @ and .com to be valid email, length check
                email = input('\nEmail: ')
                if email.lower() == 'n':
                    return 'main'
                result = UserManager.email_exists(
                    email=email)
                if result is True:  # does exist is True
                    print(f'Email: {email} is already in use.')
                    continue
                break

            while True:
                password = input('\nPasword (8 or more characters): ')
                if password == 'n':
                    return 'main'
                verify_password = input('\nType password again: ')
                if verify_password == 'n':
                    return 'main'
                result = InputManager.validate_password(
                    password=password)  # needs fail message
                if password != verify_password:
                    print('\nPasswords did not match...')
                    continue
                if result is True:
                    break
                continue

            UserManager.create(username, last_name.upper(),
                               first_name, password, email)
            input(
                f'Congratulations {first_name}, you just made an account with the bank.\nUsername: {username}\nEmail: {email}\n\nPress enter to continue to login...')
            return 'main'
