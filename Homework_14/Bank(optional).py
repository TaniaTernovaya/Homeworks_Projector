class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number
    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')
    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')
    def get_balance(self):
        return self._balance
    def get_account_number(self):
        return self._account_number
    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'

class SavingsAccount(Account):
    def __init__(self, balance, account_number, percent):
        super().__init__(balance, account_number)
        self._percent = percent
    @staticmethod
    def add_percents(account , percent):
        account._balance *= (1 + percent / 100)
        return account._balance
    
class CurrentAccount(Account):
    def __init__(self, balance, account_number, limit):
        super().__init__(balance, account_number)
        self._limit = limit
    def limit_overdraft(self):
        if self._balance <= -1 * self._limit:
            return True
        else:
            return False

account_1 = Account(200,'12345')
account_2 = Account.create_account('123456')
account_3 = Account.create_account('1234567')
account_4 = SavingsAccount(120,'1234567',5)
account_5 = CurrentAccount(120,'1234567',300)

class Bank():
    def __init__(self):
        self.accounts = []

    def open_account(self, account):
        self.accounts.append(account)
    
    def close_account(self,account):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                print(f"Account {account_number} closed successfully.")
                return
        print(f"Account {account_number} not found.")

    def pay_dividends(self, dividend_amount):
        for account in self.accounts:
            account.deposit(dividend_amount)
            print(f"Dividend of {dividend_amount} deposited into Account {account.account_number}.")

        # Specific behavior for different account types
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount) and account.limit_overdraft():
                account.send_overdraft_letter()


bank = Bank()
bank.open_account(account_1)

