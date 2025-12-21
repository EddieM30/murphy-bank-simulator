from utilities.utils import clear_console
from managers.accounts_manager import AccountsManager
from managers.input_manager import InputManager


class TransferScreen:
    def __init__(self, router):
        self.router = router

    def show(self):
        while True:
            clear_console()
            current_session = self.router.get_session
            print('=== TRANSFER BETWEEN ACCOUNTS ===\n')
            accounts = AccountsManager.list_account(
                current_session['account_nickname'])
            for i, account in enumerate(accounts):
                print(f'{i + 1}. {account}\n')

            from_account = input(
                'Which account would you like to transfer from? (input "n" to cancel): '))
            if from_account.lower() == 'n':
                return 'dashboard'
            while True:
                clear_console()
                print('=== TRANSFER BETWEEN ACCOUNTS ===')
                for i, account in enumerate(accounts):
                    print(f'{i + 1}. {account}')
                to_account= input(f'\nTransferring from {from_account} into: ')
                if to_account.lower() == 'n':
                    return 'dashboard'
                if from_account == to_account:
                    print('Can\'t transfer money to same account??')
                    input('Press enter to continue...')
                    continue
                break
            while True:
                amount= input(f'How much would you like to move from {from_account} into {to_account}?: ')
                if amount.lower() == 'n':
                    return 'dahsboard'
                deci_amount= InputManager.clean_money_amount(amount)
                if deci_amount is None:
                    continue
                placeholder = AccountsManager.transfer()

            else:
                amount= input('How much would you like to transfer?\n$')
                validate_amount= current_account.validate_money(amount)
                if validate_amount is None:
                    continue

                else:

                if current_account.transfer(
              account_name, accounts.accounts, validate_amount):
               utils.clear_console()
               print(
               f"Success!! ${validate_amount:,.2f} transferred to {account_name.title()}")
                print(f"New balance: ${current_account.balance:,.2f}")
                input('\nPress enter to continue...')
                account_menu(current_account)
                else:
                input(
                "Transfer failed - check name or amount. \nPress enter...")
