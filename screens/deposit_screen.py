from managers.accounts_manager import AccountsManager
from managers.input_manager import InputManager
from utilities.utils import clear_console


class DepositScreen:
    def __init__(self, router):
        self.router = router

    def show(self):
        while True:
            clear_console()
            current_session = self.router.get_session()
            print('=== DEPOSIT ===\n')
            print(
                f'Hey, {current_session['first_name']}! Which account are we depositing too?\n')
            accounts = AccountsManager.list_account(current_session['user_id'])
            for i, account in enumerate(accounts):
                print(f'{i + 1}. {account['account_nickname']}\n')
            try:
                choice = int(input(
                    'Please use the number value corrosponding with the account you wish to access (0 to cancel): '))
                if choice == 0:
                    return 'dashboard'
                if choice < 0 or choice > len(accounts):
                    continue

                update_account = accounts[int(choice) - 1]
                amount = input(
                    'Please enter the amount you wish to deposit (0.00): ')
                if amount == 'n':
                    return
            except ValueError:
                input('Invalid menu option.\nPress enter to continue...')
                continue

            decimal_amount = InputManager.clean_money_amount(amount)
            if decimal_amount is None:
                input('False...')
                continue

            AccountsManager.deposit(
                current_session['user_id'], update_account['account_id'], decimal_amount)
            return 'dashboard'
