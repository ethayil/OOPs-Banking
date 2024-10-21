from bank_core import BankCore


def main():
    bank_core = BankCore()  # initialising BankCore system

    print('Welcome to PyBank')
    while True:  # Loop will continue infinitly untill user enters 3(Exit)
        print('\n1. Create Account\n2. Login\n3. Exit')
        choice = input('Choose an option: ')

        if choice == '1':  # Create Account
            name = input('Enter your name: ')
            email = ''
            password = ''
            while True:
                email = input('Enter your email: ')
                if bank_core.email_exists(email):
                    print('An account with this email already exists!')
                    break
                if bank_core.is_valid_email(email):
                    break
                else:
                    print('Enter valid email')

            while True:
                password = input('Enter your password: ')
                if len(password) < 4:
                    print('Password should be greater than 3 characters')
                else:
                    break
            bank_core.create_account(name, email, password)

        elif choice == '2':  # Login
            try:
                email: str = input('Enter your email: ')
                password: str = input('Enter your password: ')
                account = bank_core.login(email, password)
                print('Logged in')

                # If logged in runs account logic
                while True:
                    print(f'\nWelcome {account.name}!')
                    print(
                        '1. Deposit\n2. Withdraw\n3. Current Balance\n4. Change Name\n5. Change Password\n6. Logout')
                    action: str = input('Choose an option: ')

                    if action == '1':  # Deposit
                        amount = float(
                            input('Enter amount to deposit: '))
                        account.deposit(amount)
                        print(f'Deposited successfully. New balance: {
                              account.balance}')

                    elif action == '2':  # Withdraw
                        amount = float(
                            input('Enter amount to withdraw: '))
                        try:
                            account.withdraw(amount)
                            print(f'Withdrawn successfully. New balance: {
                                  account.balance}')
                        except ValueError as e:
                            print(e)

                    elif action == '3':  # Check current balance
                        print(f'Current balance: {account.current_balance()}')

                    elif action == '4':
                        new_name: str = input('Enter new name: ')
                        account.change_name(new_name)

                    elif action == '5':
                        old_password: str = input('Enter old password: ')
                        new_password: str = input('Enter new password: ')
                        try:
                            account.change_password(old_password, new_password)
                        except ValueError as e:
                            print(e)

                    elif action == '6':  # Logout and break loop
                        print('Logged out successfully')
                        break
                    else:
                        # If user input is wrong re-run the loop
                        print('Invalid option. Try again.')

            except ValueError as e:  # Catch error
                print(e)

        elif choice == '3':  # Exit the main loop
            print('Exiting. Have a great day!')
            break

        else:  # If user input is wrong re-run the loop
            print('Invalid option. Try again.')


main()  # runs the main function
