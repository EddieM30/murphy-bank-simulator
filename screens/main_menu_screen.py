import sys
from screens.user_registration_screen import UserRegistration
from screens.user_login_screen import UserLogin
from utilities.utils import clear_console


class MainMenu:

    def show(self):
        while True:
            clear_console()
            options = ['New User', 'Existing User', 'Exit']

            print(
                'Welcome to Murphy\'s Trust Banking App\nPlease use numerical values to navigate menu options\n')

            for i, option in enumerate(options):
                print(f'{i + 1}. {option}')
            try:
                user_input = int(input('\nWhat would you like to do?: '))
                if user_input == 1:
                    UserRegistration.show(self)
                if user_input == 2:
                    UserLogin.show(self)
                if user_input == 3:
                    sys.exit(0)
                if user_input < 0 or user_input > 3:
                    input('Invalid menu option\nPress enter to continue...')
            except ValueError:
                input('Invalid input.\ndebug\nPress enter to continue...')


MainMenu().show()
