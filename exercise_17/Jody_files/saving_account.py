from account import Account

# Saving_Account is a kind of Account
# Saving_Account is a derived class (subclass)
# Account is a base class (superclass)
class Saving_Account(Account):

    def __init__(self, initial, interest_rate):
        super().__init__(initial)
        self._interest_rate = interest_rate


    def __str__(self):
        savings_info = self.get_holder_name()
        savings_info += "'s Savings "
        savings_info += super().__str__()
        return savings_info

    def calculate_interest(self):
        return self.getbalance() * self._interest_rate