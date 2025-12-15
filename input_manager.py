

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
