# Practice 07 — Classes and Objects

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def show_balance(self):
        print(f"{self.owner}: {self.balance:.2f} €")


account = BankAccount("Alice", 100)

account.deposit(50)
account.withdraw(30)
account.show_balance()
