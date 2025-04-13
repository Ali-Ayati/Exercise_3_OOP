from abc import ABC, abstractmethod

class Account(ABC):
    """
    Abstract base class for bank accounts.
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

    @abstractmethod
    def account_type(self):
        pass

    def __str__(self):
        return f"{self.balance:.2f}: {self.number}"


class CurrencyAccount(Account):
    """
    A subclass of Account that supports currency conversion from Rial to USD.

    Attributes:
        exchange_rate (float): Static exchange rate from Rial to USD.

    Methods:
        change_currency(amount): Converts Rial amount to USD with rounding and validation.
        transactions_in_dollar(): Returns list of all transactions converted to USD.
    """
    exchange_rate = 90000  # 1 USD = 90,000 Rial

    def __init__(self, number, balance=0):
        super().__init__(number, balance)

    @staticmethod
    def change_currency(currency_in_rial):
        if CurrencyAccount.exchange_rate <= 0:
            raise ValueError("Invalid exchange rate")
        return round(currency_in_rial / CurrencyAccount.exchange_rate, 2)

    def transactions_in_dollar(self):
        return [CurrencyAccount.change_currency(t) for t in self._transactions]
    
    def account_type(self):
        return "Currency Account"

    def __str__(self):
        return f"Business Account, Number: {self.number}, Balance: {self.balance:.2f}"