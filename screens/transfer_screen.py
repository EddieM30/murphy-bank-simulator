from utilities.utils import clear_console
from managers.accounts_manager import AccountsManager
from managers.input_manager import InputManager


class TransferScreen:
    def __init__(self, router):
        self.router = router

    def show(self):
        while True:
            clear_console()
            current_session = self.router.get_session()
            print('=== TRANSFER BETWEEN ACCOUNTS ===\n')
            accounts = AccountsManager.list_account(current_session['user_id'])
            for i, account in enumerate(accounts):
                print(f'{i + 1}. {account['account_nickname']}\n')

            choice = input(
                'Which account would you like to transfer from? (input "n" to cancel): ')
            if choice.lower() == 'n':
                return 'dashboard'
            from_account = accounts[int(choice) - 1]
            input(f'{from_account['account_nickname']}')
            while True:
                clear_console()
                print('=== TRANSFER BETWEEN ACCOUNTS ===')
                for i, account in enumerate(accounts):
                    print(f'{i + 1}. {account['account_nickname']}')
                choice = input(
                    f'\nTransferring from {from_account["account_nickname"]} into: ')
                if choice.lower() == 'n':
                    return 'dashboard'
                to_account = accounts[int(choice) - 1]
                if from_account == to_account:
                    print('Can\'t transfer money to same account??')
                    input('Press enter to continue...')
                    continue
                break
            while True:
                amount = input(
                    f'How much would you like to move from {from_account["account_nickname"]} into {to_account['account_nickname']}?: ')
                if amount.lower() == 'n':
                    return 'dahsboard'
                deci_amount = InputManager.clean_money_amount(amount)
                if deci_amount is None:
                    print(deci_amount)
                    continue
