import sys
import hashlib
import utils  # all utility methods
from user_manager import UserManager
from input_manager import InputManager
from accounts_manager import AccountsManager
from decimal import Decimal


class ScreensManager:
    '''Instantiates screen object for users'''

    def __init__(self, username: str, user_id: int, last_name: str, first_name: str, email: str) -> None:
        self.username = username
        self.user_id = user_id
        self.last_name = last_name
        self.first_name = first_name
        self.email = email

    def __str__(self):
        return f'''This session belongs too:
        \nUser ID: {self.user_id}
        \nUsername: {self.username}
        \nName: {self.first_name} {self.last_name}
        \nEmail: {self.email}'''

    @staticmethod
    def main_menu():
        while True:
            utils.clear_console()
            options = ['New User', 'Existing User', 'Exit']

            print(
                'Welcome to Murphy\'s Trust Banking App\nPlease use numerical values to navigate menu options\n')

            for i, option in enumerate(options):
                print(f'{i + 1}. {option}')
            try:
                user_input = int(input('\nWhat would you like to do?: '))
                if user_input == 1:
                    ScreensManager.create_user()
                if user_input == 2:
                    ScreensManager.user_login()
                if user_input == 3:
                    sys.exit(0)
                if user_input < 0 or user_input > 3:
                    input('Invalid menu option\nPress enter to continue...')
            except ValueError:
                input('Invalid input.\ndebug\nPress enter to continue...')

    @staticmethod
    def create_user():
        while True:
            utils.clear_console()
            print("=== USER PROFILE ===")
            print('\nAt any point, input "n" to cancel.')

            while True:
                first_name = input('\nFirst Name: ').strip()
                if first_name.lower() == 'n':
                    return
                last_name = input('\nLast Name: ').strip()
                if last_name.lower() == 'n':
                    return
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
                    return
                result = UserManager.username_exists(username=username)
                if result is True:  # does exist is True
                    print(f'Username: {username} is already taken.')
                    continue
                break

            while True:  # Needs checks for @ and .com to be valid email, length check
                email = input('\nEmail: ')
                if email.lower() == 'n':
                    return
                result = UserManager.email_exists(
                    email=email)
                if result is True:  # does exist is True
                    print(f'Email: {email} is already in use.')
                    continue
                break

            while True:
                password = input('\nPasword (8 or more characters): ')
                if password == 'n':
                    return
                verify_password = input('\nType password again: ')
                if verify_password == 'n':
                    return
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
            return

    @staticmethod
    def user_login():
        while True:
            utils.clear_console()
            print('==== Login ====')
            print('\nInput "n" anywhere to return to main menu.')
            username = input('\nUsername: ')
            if username.lower() == 'n':
                return
            password = input('\nPassword: ')
            if password == 'n':
                return

            user = UserManager.authenticate(username, password)
            if user is None:
                input(
                    'Invalid username or password. Try again.\nPress enter to continue...')
                continue
            utils.clear_console()

            current_session = ScreensManager(
                user['username'], user['user_id'], user['last_name'].title(), user['first_name'], user['email'])
            ScreensManager.dashboard(current_session=current_session)
            input('Incorrect password.\nPress enter to continue...')

    @staticmethod
    def dashboard(current_session):
        while True:
            utils.clear_console()
            accounts = AccountsManager.list_account(current_session.user_id)
            if len(accounts) == 0:  # if no accounts forces account creation
                ScreensManager.create_account(current_session)
                continue

            print('=== User Menu ===\n')
            print(f'Welcome, {current_session.first_name}\n')

            for account in reversed(accounts):
                deci_bal = Decimal(account['balance'])
                print(
                    f'{account['account_nickname']} {account['account_type'].title()} balance: ${deci_bal:,.2f}\n')

            options = ['Deposit', 'Withdraw', 'Transfer',
                       'Open new account', 'Logout of session']
            for i, option in enumerate(options):
                print(f'{i + 1}. {option}')
            try:
                choice = int(input('\nWhat would you like to do? '))
                if choice == 1:
                    ScreensManager.deposit_menu(current_session)
                if choice == 2:
                    ScreensManager.withdraw_menu(current_session)
                if choice == 3:
                    ScreensManager.transfer_menu(current_session)
                if choice == 4:
                    ScreensManager.create_account(current_session)
                if choice == 5:
                    current_session = None
                    return
            except ValueError:
                input('Invalid input.\nPress enter to continue...')
                continue

    @staticmethod
    # returns to stale dashboard upon first account creation but none after that
    def create_account(current_session):
        while True:
            utils.clear_console()
            print('=== Create an Account ===')
            print('\nWhat king of account would you like to setup?\n')
            options = ['Checking', 'Savings', 'Credit']
            for i, option in enumerate(options):
                print(f'{i + 1}. {option}')

            choice = input('Type "n" to cancel anytime... ')
            if choice == 'n':
                return
            if int(choice) == 1:
                nickname = input('\nA nickname is needed for this account: ')
                AccountsManager.create_account(
                    current_session.user_id, 'checking', nickname)
                return
            if int(choice) == 2:
                nickname = input('\nA nickname is needed for this account: ')
                AccountsManager.create_account(
                    current_session.user_id, 'savings', nickname)
                return
            if int(choice) == 3:
                nickname = input('\nA nickname is needed for this account: ')
                AccountsManager.create_account(
                    current_session.user_id, 'credit', nickname)
                return

    @staticmethod
    def deposit_menu(current_session):
        while True:
            utils.clear_console()
            print('=== DEPOSIT ===\n')
            print(
                f'Hey, {current_session.first_name}! Which account are we depositing too?\n')
            accounts = AccountsManager.list_account(current_session.user_id)
            for i, account in enumerate(accounts):
                print(f'{i + 1}. {account['account_nickname']}\n')
            try:
                choice = int(input(
                    'Please use the number value corrosponding with the account you wish to access: '))
                if str(choice) == 'n':
                    return
                if choice > len(accounts) or choice < len(accounts):
                    continue
                update_account = accounts[int(choice) - 1]
                amount = input(
                    'Please enter the amount you wish to deposit (0.00): ')
            except ValueError:
                input('Invalid menu option.\nPress enter to continue...')

            input('Testing')

    @staticmethod
    def withdraw_menu(current_session):
        while True:
            input('withdraw')
            return

    @staticmethod
    def transfer_menu(current_session):
        while True:
            input('transfer')
            return
