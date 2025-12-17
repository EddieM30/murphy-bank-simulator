from utilities.utils import clear_console
from managers.user_manager import UserManager
from managers.screen_manager import ScreensManager
from main import router
from .router import ScreenRouter


class UserLogin:
    def show(self):
        while True:
            clear_console()
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
            clear_console()

            router.current_session = user
            return 'dashboard'
