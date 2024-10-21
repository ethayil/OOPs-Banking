class Account:
    def __init__(self, name: str, email: str, password: str, account_number: int, balance: float = 0.0):
        self.name = name
        self.email = email
        self.password = password
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float):  # Deposit amount
        self.balance += amount

    def withdraw(self, amount: float):  # Withdraw amount
        if (self.balance <= amount):  # Check if amount is greater than the current balance
            raise ValueError('Insufficient funds')
        else:
            self.balance -= amount

    def current_balance(self):  # Get current balance
        return self.balance

    def change_name(self, new_name: str):
        self.name = new_name
        print(f'Name changed to {self.name}')

    def change_password(self, old_password: str, new_password: str):
        if self.password == old_password:
            self.password = new_password
            print('Password changed successfully')
        else:
            raise ValueError('Incorrect old password')

    def __str__(self) -> str:
        return f'Account #{self.account_number} - {self.name} - Balance: {self.balance}'
