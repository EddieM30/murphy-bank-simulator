from utilities.utils import clear_console
from managers.accounts_manager import AccountsManager
from decimal import Decimal


class UserDashboard:
    def __init__(self, router):
        self.router = router

    def show(self):
        while True:
            clear_console()
            session = self.router.get_session()
            accounts = AccountsManager.list_account(session['user_id'])
            if len(accounts) == 0:  # if no accounts forces account creation
                return 'account creation'

            print('=== User Menu ===\n')
            print(f'Welcome, {session['first_name']}\n')

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
                    return 'deposit'
                if choice == 2:
                    return 'withdraw'
                if choice == 3:
                    return 'transfer'
                if choice == 4:
                    return 'create account'
                if choice == 5:
                    return 'logout'

            except ValueError:
                input('Invalid input.\nPress enter to continue...')
                continue
