import re
from typing import Dict
from account import Account


class BankCore:
    account_counter = 22222  # initialise account numbers from 1000 onwards

    def __init__(self):
        self.accounts: Dict[int, Account] = {}

    def is_valid_email(self, email: str):  # Regex to check if email is valid
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    def email_exists(self, email: str):  # Check if email already exists
        for account in self.accounts.values():
            if account.email == email:
                return True
            else:
                return False

    def create_account(self, name: str, email: str, password: str):  # Create account
        if self.email_exists(email):  # Check if email already exists
            print('An account with this email already exists!')
            return

        if not (self.is_valid_email(email)):  # Check if email is valid
            print('Enter a valid email!')
            return

        # create account if there are no issues
        try:
            self.accounts[self.account_counter] = Account(
                name, email, password, account_number=self.account_counter)
            print(f'Account created successfully. Your account number is: {
                  self.account_counter}')
            self.account_counter += 1  # Increment account counter after successful account creation
        except ValueError as e:  # Catch exceptions
            print(e)

    def login(self, email, password):  # Login logic
        for account in self.accounts.values():
            if account.email == email and account.password == password:  # Find account by email
                return account
        raise ValueError('Invalid email or password')
