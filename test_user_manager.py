from database import initialize_databases, get_connection
from user_manager import UserManager
from accounts_manager import AccountsManager
from decimal import Decimal

# user = UserManager.create('badboi3', 'COWELL', 'Simon',
#                         'hacker11', 'example@email.com')
# print(dict(user))


user = AccountsManager.list_account(2)

user = AccountsManager.show_balance(2, 1)
print(user)

amount = Decimal(5000).quantize(Decimal('0.01'))
user = AccountsManager.withdraw(2, 1, amount)


print(user)
