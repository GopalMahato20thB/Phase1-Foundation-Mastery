#2. Build a `BankAccount` class with attributes `account_number`, `balance`, and method `deposit()` and `withdraw()`.
class BankAccount:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, balance):
        if balance < 0:
            print("balance must be greater than Zero!")
        self.balance += balance

    def withdraw(self, balance):
        if balance > self.balance:
            print("Insufficient Funds!")
        self.balance -= balance

    def check_balance(self):
        return f"Current balance: {self.balance}"

gopal = BankAccount(82342823748, 12)
print(gopal.check_balance())
gopal.deposit(50)
print(gopal.check_balance())
