class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self
    
    def transfer_money(self, friend, amount):
        self.account_balance -= amount
        friend.account_balance += amount
        print(f"User: {self.name}, Balance: {self.account_balance}")
        print(f"User: {friend.name}, Balance: {friend.account_balance}")
        return self
        

Nick = User("Nick")
Malcolm = User("Malcolm")
Dennis = User("Dennis")

Nick.make_deposit(68000).make_deposit(3200).make_deposit(4000).make_withdrawal(300).display_user_balance()

Malcolm.make_deposit(14000).make_deposit(32000).make_withdrawal(7300).make_withdrawal(1000).display_user_balance()

Dennis.make_deposit(10000).make_withdrawal(500).make_withdrawal(100).display_user_balance()

Nick.transfer_money(Dennis, 10000)
