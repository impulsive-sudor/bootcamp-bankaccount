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

bob = BankAccount(0.03, 200)
bob.deposit(300).deposit(400).withdraw(500).yield_interest().display_account_info()

john = BankAccount(0.03, 400)
john.deposit(40).deposit(50).withdraw(10).withdraw(5).withdraw(2).withdraw(1).yield_interest().display_account_info()