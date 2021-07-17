class user:
    def __init__(self, username, email):
            self.username = username
            self.email = email
            self.account = BankAccount(int_rate=0.02, balance=20)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()


class BankAccount:
	def __init__(self, int_rate=0, balance=0):
            self.int_rate = int_rate
            self.balance = balance

	def deposit(self, amount):
            self.balance += amount
            return self
        
	def withdraw(self, amount):
            if self.balance < amount:
                print("Insufficient funds: Charging a $5 fee")
                self.balance -= 5
            if self.balance >= amount:
                self.balance -= amount
            return self
	def display_account_info(self):
            print(f"Balance: {self.balance}")

	def yield_interest(self):
            if self.balance > 0:
                self.balance = self.balance * self.int_rate + self.balance
            return self

bob = user("bob", "bob@dogbot")

bob.make_deposit(200).display_user_balance()