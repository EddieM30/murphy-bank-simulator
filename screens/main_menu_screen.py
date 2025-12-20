from utilities.utils import clear_console


class MainMenu:
    def __init__(self, router):
        self.router = router

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
                    return 'register'
                if user_input == 2:
                    return 'login'
                if user_input == 3:
                    return 'exit'
                if user_input < 0 or user_input > 3:
                    input('Invalid menu option\nPress enter to continue...')
            except ValueError:
                input('Invalid input.\ndebug\nPress enter to continue...')
