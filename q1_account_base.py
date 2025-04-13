from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, number: int, balance: float = 0.0):
        self.number = number
        self.balance = balance
        self._transactions = []

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
        self._transactions.append(amount)

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        self._transactions.append(-amount)

    def __str__(self):
        return f"{self.balance:.2f}: {self.number}"

    @abstractmethod
    def account_type(self):
        """This method should be implemented in child classes to define account type."""
        pass
      
# کلاس فرزند برای تست عملکرد. این بخش به بعد شامل مسئله فعلی نیست.
class SavingsAccount(Account):
    def account_type(self):
        return "Savings Account"

account = SavingsAccount("123456", 500.0)
print(account)

account.deposit(100)
print(account)

account.withdraw(200)
print(account)

try:
    account.withdraw(450)
except ValueError as e:
    print(e)