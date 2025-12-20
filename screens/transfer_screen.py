from utilities.utils import clear_console
from managers.accounts_manager import AccountsManager


class TransferScreen:
    def __init__(self, router):
        self.router = router

    def show(self):
        while True:
            clear_console()
            current_session = self.router.get_session
            print('=== TRANSFER ===\n')
            accounts = AccountsManager.list_account(current_session['user_id'])
            for i, account in enumerate(accounts):
                print(f'{i + 1}. {account['account_nickname']}\n')
            account_name = input(
                'Please type the name of the account you want to transfer funds to (input "n" to cancel): ')
            if account_name.lower() == 'n':
                return 'dashboard'
            elif account_name.lower() == current_account.owner.lower():
                input(
                    'You can\'t transfer money to the currently active account.\nPress enter to continue...')
                continue
            else:
                amount = input('How much would you like to transfer?\n$')
                validate_amount = current_account.validate_money(amount)
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
