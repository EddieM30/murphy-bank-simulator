from decimal import Decimal, InvalidOperation


class InputManager:
    '''Validate user input'''

    @staticmethod
    def validate_name(first_name: str, last_name: str) -> bool:
        if len(first_name) <= 0 or len(last_name) <= 0:
            return False
        if any(char.isdigit() for char in first_name):
            return False
        if any(char.isdigit() for char in last_name):
            return False
        if any(not char.isalnum() and not char.isspace() for char in first_name):
            return False
        if any(not char.isalnum() and not char.isspace() for char in last_name):
            return False
        return True

    @staticmethod
    def validate_password(password: str) -> bool:
        if len(password) >= 8:
            return True
        return False

    @staticmethod
    def clean_money_amount(raw_amount: str) -> Decimal | None:
        cleaned_amount = raw_amount.strip().replace('$', '').replace(',', '')
        if '.' in cleaned_amount:
            whole, cents = cleaned_amount.split('.')
            if len(cents) > 2:
                input(
                    'Cents cannot have a greater value than .99\nPress enter to continue...')
                return None
        try:
            decimal_amount = Decimal(cleaned_amount)
            print(decimal_amount)
            return decimal_amount
        except InvalidOperation as e:
            print(f'Invalid operation: {e}')
            print("The input could not be converted to a valid Decimal number.")
            return None
