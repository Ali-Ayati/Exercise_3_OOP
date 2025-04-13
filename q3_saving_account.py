from abc import ABC, abstractmethod

class Account(ABC):
    """
    Abstract base class for bank accounts.

    Attributes:
        number (int): Account number.
        balance (float): Current balance of the account.
        _transactions (list): List of all transaction amounts (positive for deposits, negative for withdrawals).
        _total_deposit (float): Sum of all deposits.
        _total_withdraw (float): Sum of all withdrawals.

    Methods:
        deposit(amount): Adds a positive amount to the balance and tracks the transaction.
        withdraw(amount): Deducts amount from balance if sufficient and tracks the transaction.
        account_type(): Abstract method to define account type in child classes.
    """
    def __init__(self, number: int, balance: float = 0.0):
        self.number = number
        self.balance = balance
        self._transactions = []
        self._total_deposit = 0.0
        self._total_withdraw = 0.0

    def deposit(self, amount: float):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Amount must be a positive number.")
        self.balance += amount
        self._transactions.append(amount)
        self._total_deposit += amount

    def withdraw(self, amount: float):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Amount must be a positive number.")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        self._transactions.append(-amount)
        self._total_withdraw += amount

    @abstractmethod
    def account_type(self):
        pass

    def __str__(self):
        return f"{self.balance:.2f}: {self.number}"


class SavingAccount(Account):
    """
    A subclass of Account that represents a savings account.

    Includes a method to calculate the ratio of total income (deposits) to expenses (withdrawals).

    Methods:
        calculate_income_to_expense_ratio():
            Returns a formatted string showing total deposits, withdrawals, difference,
            and their ratio.
        account_type():
            Returns a string identifying the type of account.
    """
    def account_type(self):
        return "Saving Account"

    def calculate_income_to_expense_ratio(self):
        if self._total_withdraw == 0:
            ratio = 0
        else:
            ratio = self._total_deposit / self._total_withdraw
        difference = self._total_deposit - self._total_withdraw
        return (
            f"Withdraws: {self._total_withdraw} | Deposits: {self._total_deposit}\n"
            f"Difference: {difference} | Ratio: {ratio:.2f}"
        )

    def __str__(self):
        return f"Saving Account, Number: {self.number}, Balance: {self.balance:.2f}"
      
# تست عملکرد: 
acc = SavingAccount(1234, 100000)
acc.deposit(2000)
acc.deposit(1000)
acc.withdraw(1500)
acc.withdraw(2500)
print(acc.calculate_income_to_expense_ratio())
print(acc)