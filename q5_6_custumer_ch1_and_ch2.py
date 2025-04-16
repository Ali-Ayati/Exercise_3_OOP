from abc import ABC, abstractmethod

class Account(ABC):
    """
    Abstract base class for bank accounts.

    This class serves as the foundational structure for all specific account types such as
    SavingAccount, CheckingAccount, and CurrencyAccount. It handles basic transaction tracking
    and enforces implementation of account-specific behavior through abstract methods.

    Attributes:
        number (int): Unique account number.
        balance (float): Current balance in the account.
        _transactions (list of float): List storing all transaction amounts. Positive for deposits,
                                       negative for withdrawals.

    Methods:
        deposit(amount): Adds a valid positive amount to the balance and stores the transaction.
        withdraw(amount): Deducts a valid amount from balance if sufficient, and stores the transaction.
        transactions_checking(): Abstract method to be implemented in child classes for analyzing transactions.
        __iadd__(amount): Enables the use of += to deposit funds.
        __isub__(amount): Enables the use of -= to withdraw funds.
        __eq__(other): Compares two accounts for equality based on balance.
        __lt__(other): Allows sorting and comparison of accounts based on balance.
        __add__(other): Adds numeric value to the account balance using + operator.
        __str__(): Returns a formatted string representation of the account.
    """
    def __init__(self, number: int, balance: float = 0.0):
        self.number = number
        self.balance = balance
        self._transactions = []

    def deposit(self, amount: float):
        if amount > 0.0:
            self.balance += amount
            self._transactions.append(amount)
        else:
            raise ValueError("Amount must be positive")

    def withdraw(self, amount: float):
        if amount > 0.0:
            if amount <= self.balance:
                self.balance -= amount
                self._transactions.append(-amount)
            else:
                print("موجودی کافی نیست")
        else:
            raise ValueError("Amount must be positive")
  
    @abstractmethod
    def transactions_checking(self, transactions):
        pass

    def __iadd__(self, amount):
        # امکان استفاده از +=
        self.deposit(amount)
        return self
        
    def __isub__(self, amount):
        # امکان استفاده از -=
        self.withdraw(amount)
        return self

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __add__(self, other):
        if isinstance(other, (int, float)):
            self.deposit(other)
            return self
        raise TypeError("Only numeric values can be added to an account.")
    def __str__(self):
        return f"{self.number} : {self.balance:.2f}"
    
    def show_account_balance(self) -> int | float:
        return self.balance
    
    def show_transactions(self) -> list:
        return self._transactions

# hesab pas andaz
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
    def __init__(self, number, balance = 0):
      super().__init__(number, balance)
      
    def transactions_checking(self):
        withdraw_sa = 0
        deposit_sa = 0
        for i in self._transactions:
            if i < 0:
                withdraw_sa += abs(i)
            else:
                deposit_sa += i
                
        difference = withdraw_sa - deposit_sa
        nesbat = deposit_sa/withdraw_sa if withdraw_sa != 0 else 0
        
        return (
            f"Withdraws: {withdraw_sa} | Deposts: {deposit_sa}\n" 
                f"Difference: {difference} | nesbat: {nesbat:.2f}"
                )
            
    def __str__(self):
       return f"Saving Account, Number: {self.number}, Balance: {self.balance:.2f}"

# hesab jary
class CheckingAccount(Account):
    """
    Subclass of Account that requires a minimum initial balance.
    Represents a checking account with custom string formatting.
    """
    min_amount = 100000
    def __init__(self, number, balance = 0.0):
        if balance < self.min_amount:
            raise ValueError(f"موجودیه اولیه نباید کم تر از {CheckingAccount.min_amount} باشد.")
        super().__init__(number, balance)
        
    def transactions_checking(self, transactions):
      pass
    
    def __str__(self):
       return f"Checking Account, Number: {self.number}, Balance: {self.balance:.2f}"
            

# hesab arzi
class CurrencyAccount(Account):
    """
    A subclass of Account that supports currency conversion from Rial to USD.

    Attributes:
        exchange_rate (float): Static exchange rate from Rial to USD.

    Methods:
        change_currency(amount): Converts Rial amount to USD with rounding and validation.
        transactions_in_dollar(): Returns list of all transactions converted to USD.
    """
    exchange_rate = 90000
    
    def __init__(self, number, balance = 0):
      super().__init__(number, balance)
      
    
    @staticmethod
    def change_currency(currency_in_rial):
        changed_currency = currency_in_rial / CurrencyAccount.exchange_rate
        return changed_currency        
    
    def transactions_in_dollar(self):
        transactions_dollar_list = []
        
        for t in self._transactions:
            dollar_currency = CurrencyAccount.change_currency(t)
            transactions_dollar_list.append(dollar_currency)
            
        return transactions_dollar_list
            
    def transactions_checking(self, transactions):
      pass
    
    def __str__(self):
      return f"Business Account, Number: {self.number}, Balance: {self.balance:.2f}"
  


class Customer:
    """
    Represents a bank customer who can hold multiple accounts.

    Attributes:
        name (str): Customer's name
        ssn (int): Customer's national ID
        accounts (dict): Dictionary of account type keys to account objects
    """
    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn
        self.accounts = {}  # {'S': SavingAccount, 'B': CheckingAccount, 'C': CurrencyAccount}

    def open_account(self, acc_type, number, balance):
        if acc_type not in ("S", "B", "C"):
            raise ValueError("Invalid account type. Must be one of: 'S', 'B', or 'C'.")
        
        if acc_type == "S":
            self.accounts[acc_type] = SavingAccount(number, balance)
        elif acc_type == "B":
            self.accounts[acc_type] = CheckingAccount(number, balance)
        elif acc_type == "C":
            self.accounts[acc_type] = CurrencyAccount(number, balance)

    def make_deposit(self, acc_type, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if acc_type in self.accounts:
            self.accounts[acc_type] += amount
        else:
            raise ValueError("No such account found.")

    def make_withdraw(self, acc_type, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if acc_type in self.accounts:
            self.accounts[acc_type] -= amount
        else:
            raise ValueError("No such account found.")

    def make_transfer(self, source_type, dest_account, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if source_type not in self.accounts:
            raise ValueError("Source account not found.")
        if not isinstance(dest_account, Account):
            raise TypeError("Destination must be an Account instance.")

        if amount > self.accounts[source_type].balance:
            raise ValueError("Insufficient funds.")

        self.accounts[source_type] -= amount
        dest_account += amount

        return (
            f"Transfer successful!\n"
            f"Source balance: {self.accounts[source_type].balance:.2f}\n"
            f"Destination balance: {dest_account.balance:.2f}"
        )

    def __str__(self):
        if not self.accounts:
            return f"Customer: {self.name}, SSN: {self.ssn} | No accounts available."
        info = f"Customer: {self.name}, SSN: {self.ssn}\nAccounts:\n"
        for acc_type, acc in self.accounts.items():
            info += f"  - {acc}\n"
        return info.strip()
    
    def get_balance(self, acc_type):
        if acc_type in self.accounts:
            return self.accounts[acc_type].show_account_balance()
        raise ValueError("Account type not found.")
    
    def get_transactions(self, acc_type):
        if acc_type in self.accounts:
            return self.accounts[acc_type].show_transactions()
        raise ValueError("Account type not found.")
    

# تست عملکرد:
c1 = Customer("Ali", 1234)
c1.open_account("S", 1001, 500000)
c1.open_account("C", 1002, 200000)

c1.make_deposit("S", 50000)
c1.make_withdraw("S", 10000)

c2 = Customer("Sara", 2222)
c2.open_account("S", 2001, 100000)

print(c1.make_transfer("S", c2.accounts["S"], 25000))

print(c1)
print(c2)

if c1.accounts["S"] < c2.accounts["S"]:
    print("Customer 1's saving account has less balance than Customer 2's saving account.")
else:
    print("Customer 2's saving account has less balance than Customer 1's saving account.")
    
print(c1.get_balance("S"))
print(c1.get_transactions("S"))