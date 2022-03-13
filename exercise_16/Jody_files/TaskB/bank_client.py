from savings_account import SavingAccount
from current_account import CurrentAccount
from account import Account

# create instance of a savings account
jody_saving = SavingAccount(100, 1.5)
# deposit into savings account
jody_saving.deposit(400)
# set account holder name
jody_saving.set_holder_name("Jody")
# print(jody_saving.getbalance())
print(jody_saving)

# create instance of a current account
jody_current = CurrentAccount(500, 250)
# set account holder name
jody_current.set_holder_name("Jody Broad")
# print account holder name
print(jody_current.get_holder_name())
# print current account balance
print(jody_current.getbalance())

# deposit into current account
jody_current.deposit(100)
# set current account description
jody_current.description = "Jody's current account"   # setter gets called
# get current account description and save to a variable
desc = jody_current.description   # getter gets called
# print this
print(desc)

# withdraw from current account
jody_current.withdraw(50)
# print new balance
print(jody_current.getbalance())

# create new instance of a current account
emily_current = CurrentAccount(800, 0)
# deposit into current account
emily_current.deposit(50)
# set account holder name
emily_current.set_holder_name("Emily Field")
# print account holder name
print(emily_current.get_holder_name())

# set account description
emily_current.description = "Emily's current account"
# print account description
print(emily_current.description)


# withdraw more than is in the account, will display error message
emily_current.withdraw(1050)
# print current balance
print(emily_current.getbalance())