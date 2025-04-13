from abc import ABC, abstractmethod

class Account(ABC):
    """
    Abstract base class representing a generic bank account.
    """
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


class CheckingAccount(Account):
    """
    Subclass of Account that requires a minimum initial balance.
    Represents a checking account with custom string formatting.
    """
    min_amount = 100000

    def __init__(self, number: int, balance: float = 0.0):
        if not isinstance(balance, (int, float)):
            raise TypeError("Balance must be a numeric value.")
        if balance < self.min_amount:
            raise ValueError(f"Initial balance must be at least {self.min_amount}.")
        super().__init__(number, balance)

    def __str__(self):
        return f"Checking Account, Number: {self.number}, Balance: {self.balance:.2f}"

    def account_type(self):
        return "Checking Account"
            
      
# تست عملکرد
acount = CheckingAccount(1234, 100000)
print(acount)