import sys
from .account_creation import AccountCreation
from .deposit_screen import DepositScreen
from .main_menu_screen import MainMenu
from .transfer_screen import TransferScreen
from .user_dashboard import UserDashboard
from .user_login_screen import UserLogin
from .user_registration_screen import UserRegistration
from .withdraw_screen import WithdrawScreen

# Mapping of route names to screen classes for easy lookup and clearer routing
SCREEN_MAP = {
    "main_menu": MainMenu,
    "account_creation": AccountCreation,
    "deposit": DepositScreen,
    "transfer": TransferScreen,
    "dashboard": UserDashboard,
    "login": UserLogin,
    "register": UserRegistration,
    "withdraw": WithdrawScreen,
}


class ScreenRouter:
    def __init__(self):
        self.session = None
        self.current_screen = None

    def run(self):
        while True:
            if self.current_screen is None:
                self.current_screen = MainMenu()

            next_action = self.current_screen.show(self)
            if next_action == 'register':
                self.current_screen = UserRegistration.show(self)
            elif next_action == 'login':
                self.current_screen == UserLogin.show(self)
            elif self.current_screen == 'exit':
                sys.exit(0)
            else:
                continue
