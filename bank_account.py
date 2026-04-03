def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Done: {func.__name__}")
        return result
    return wrapper

class BankAccount:

    bank_name = "National Bank"
    total_accounts = 0
    
    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
        BankAccount.total_accounts += 1

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value
    
    def __str__(self):
        return f"Account holder: {self.owner}, Account balance: {self.balance}"

    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self.balance})"

    @log_call
    def deposit(self, amount):
        if BankAccount.is_valid_amount(amount):
            self.balance += amount
            print(f"{amount} deposited!\nYour new Balance is: {self.balance}")
        else:
            raise ValueError("Amount must be positive")
    
    @log_call
    def withdraw(self, amount):
        if BankAccount.is_valid_amount(amount):
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount} withdrawn!\nYour new Balance is: {self.balance}")
            else:
                raise ValueError("Insufficient funds")
        else:
                raise ValueError("Amount must be positive")
        

    




class SavingsAccount(BankAccount):
    def __init__(self,owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.intrest_rate = interest_rate
    
    def apply_interest(self):
        self.balance = self.balance + (self.balance * self.intrest_rate)

moAccount = BankAccount("mohammed", 100)
moAccount.deposit(100)
moAccount.balance
try:
    moAccount.deposit(-200)
except ValueError as e:
    print(f"Transaction failed: {e}")
finally:
    print("Transaction attempt done.")
try:
    moAccount.withdraw(3434343)
except ValueError as e:
    print(f"Transaction failed: {e}")
finally:
    print("Transaction attempt done.")