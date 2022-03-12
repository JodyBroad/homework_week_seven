from account import Account

another = Account(5)

another.set_holder_name("Fred Flintstone")

print(another.get_holder_name())


another.deposit(100)

another.description = "Fred's description" # setter gets called
desc = another.description # getter gets called
print(desc)



wilma = Account(800)
wilma.deposit(50)
wilma.set_holder_name("Wilma")
print(wilma.get_holder_name())

wilma.description = "Wilma Flintstone from Bedrock"
print(wilma.description)