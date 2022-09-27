class BankAccount:
    all_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self
    def withdraw(self, amount):
        # your code here
        if self.balance <= 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
            
        return self
    def display_account_info(self):
        # your code here
        print(f"Interest Rate: {self.int_rate}, Balance: {self.balance}")
    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1+self.int_rate)
        return self
        # your code here
    def __repr__(self):
        return f"Interest Rate: {self.int_rate}, Balance: {self.balance}"

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance = 0)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(f"Balance: ${self.account.balance}")
        
    def transfer_money(self, amount, other_user):
        self.account.balance -= amount
        other_user.account.balance += amount
        return other_user.account.balance

brandon = User("brandon", "brandon@gmail.com")
chris = User("chris", "chris@gmail.com")

print(chris.email)
print(brandon.email)


brandon.make_deposit(300).make_deposit(200).make_deposit(300).make_withdrawal(400)
chris.make_deposit(1000).make_deposit(300).make_withdrawal(300).make_withdrawal(1000).make_withdrawal(200).make_withdrawal(200)
brandon.display_user_balance()
chris.display_user_balance()
brandon.transfer_money(300, chris)
brandon.display_user_balance()
chris.display_user_balance()

# for one_account in BankAccount.all_accounts:
#     one_account.display_account_info()
