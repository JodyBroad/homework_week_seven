from account import Account
from savings_account import SavingAccount
from current_account import CurrentAccount

class MyErrors(Exception):
    # base class for other exceptions
    pass

# class InsufficientFundsException(Exception):
#     # raised when customer tries to withdraw more money than they have in the account
#     def withdraw_check(self, amount):
#         self.__balance = balance
#     raise InsufficientFundsException('insufficient funds')