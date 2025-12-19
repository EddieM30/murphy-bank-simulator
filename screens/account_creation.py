from utilities.utils import clear_console
from managers.accounts_manager import AccountsManager


class AccountCreation:
    def __init__(self, router):
        self.router = router

    def show(self):
        while True:
            clear_console()
            current_session = self.router.get_session()
            print('=== Create an Account ===')
            print('\nWhat king of account would you like to setup?\n')
            options = ['Checking', 'Savings', 'Credit']
            for i, option in enumerate(options):
                print(f'{i + 1}. {option}')

            choice = input('Type "n" to cancel anytime... ')
            if choice == 'n':
                return 'main'
            if int(choice) == 1:
                nickname = input('\nA nickname is needed for this account: ')
                AccountsManager.create_account(
                    current_session['user_id'], 'checking', nickname)
                return
            if int(choice) == 2:
                nickname = input('\nA nickname is needed for this account: ')
                AccountsManager.create_account(
                    current_session['user_id'], 'savings', nickname)
                return
            if int(choice) == 3:
                nickname = input('\nA nickname is needed for this account: ')
                AccountsManager.create_account(
                    current_session['user_id'], 'credit', nickname)
                return
