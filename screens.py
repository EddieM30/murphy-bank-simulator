import sys
import utils  # helper functions for clearing the console to provide a clean menu look
import bank_account
import accounts  # list of current BankAccount objects


def main_menu() -> None:
    """ Main entry point - runs the entire application """
    while True:
        utils.clear_console()
        print('Welcome to Murphy Bank – Console Banking System ')
        try:
            user_input = int(
                input("1. Create new account\n2. Log in to account\n3. Exit\n"))
        except ValueError:
            print('Please navigate the menu using numerical input')
            input('Press enter to continue...')
            continue

        if user_input == 1:
            create_account()
        elif user_input == 2:
            login_screen()
        elif user_input == 3:
            sys.exit(0)
        else:
            print("Invalid input.")
            input('Press enter to continue...')
            continue


def create_account() -> None:
    """ Guide user through creating a new bank account """
    while True:
        utils.clear_console()
        print('At any point during account creation input "n" to cancel.')
        owner = input("Name (must be greater than 0 characters): ")
        if owner.lower() == 'n':
            return
        elif len(owner) < 1:
            continue
        password = input('Password (must be at least 6 characters long): ')
        if password.lower() == 'n':
            return
        elif len(password) < 6:
            continue
        else:
            break

    while True:
        raw = input(
            "Deposit ($00.00): $").strip().replace(',', '')
        if raw.lower() == 'n':
            return
        init_deposit = bank_account.BankAccount.validate_money(raw)
        if init_deposit is not None:
            break

    new_bank_account = bank_account.BankAccount(
        owner, init_deposit, password)
    new_bank_account.print_account()
    input('Press enter to continue...')
    accounts.accounts.append(new_bank_account)
    return


def login_screen() -> None:
    """Display account list and handle login with password check"""
    utils.clear_console()
    while True:
        for num, account in enumerate(accounts.accounts):
            print(f'{num + 1}. {account.owner}')

        account_name = input(
            'Please type the name of the account you want to access (type "n" to cancel): ')
        if account_name.lower() == 'n':
            return
        password = input('Enter password: ')

        for account in accounts.accounts:
            if account_name.lower() == account.owner.lower():
                if password == account.password:
                    accounts.logged_in_as = account.owner
                    account_menu(account)
                else:
                    print('Wrong account name or password. Try again.')
                    input('Press enter to continue')


def account_menu(current_account) -> None:
    """Main account dashboard after successful login"""
    while True:
        utils.clear_console()

        print(f'Logged in as: {current_account.owner}')
        print(f'Available balance: {current_account.balance:,.2f}\n')
        try:
            user_input = int(
                input("1. Deposit\n2. Withdraw\n3. Transfer\n4. Show Balance\n5. Logout\n"))

            if user_input == 1:
                deposit_screen(current_account)
            elif user_input == 2:
                withdraw_screen(current_account)
            elif user_input == 3:
                transfer_screen(current_account, accounts)
            elif user_input == 4:
                current_account.show_balance()
            elif user_input == 5:
                return
        except ValueError:
            input("Invald option. Press enter to continue...")
            continue


def deposit_screen(account) -> None:
    """Handle deposit with 'n' to cancel"""
    while True:
        utils.clear_console()
        print('Input "n" to cancel transaction.')

        amount = input(
            'How much would you like to deposit?\n$').strip().replace(',', '')
        if amount.lower() == 'n':
            return
        validated_amount = account.validate_money(amount)
        if validated_amount is None:
            continue

        account.deposit(validated_amount)
        break


def withdraw_screen(account) -> None:
    """Handle withdrawal with 'n' to cancel"""
    while True:
        utils.clear_console()
        print('Input "n" to cancel transaction.')
        amount = input('How much would you like to withdraw?\n$')
        if amount.lower() == 'n':
            return
        validated_amount = account.validate_money(amount)

        if validated_amount is None:
            continue

        account.withdraw(validated_amount)
        break


def transfer_screen(current_account, accounts) -> None:
    """Handle transfers between existing accounts"""
    while True:
        utils.clear_console()
        for i, account in enumerate(accounts.accounts):
            print(f'{i}. {account.owner}')
        account_name = input(
            'Please type the name of the account you want to transfer funds to (input "n" to cancel): ')
        if account_name.lower() == 'n':
            return
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
                    return
                else:
                    input("Transfer failed - check name or amount. \nPress enter...")


main_menu()
