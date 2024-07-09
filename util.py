import csv
import os
import re
from account import Account

# .CSV READ/WRITE
###################################################

# Create default .csv file *****
def create_bank():
    admin_account = ['000', '', '', 'admin', 'admin', '']
    with open('./accounts.csv', 'w',newline="") as file:
        csv_writer=csv.writer(file)
        csv_writer.writerow(admin_account)

# Open .csv and retrieve rows ****
def retrieve_accounts():
    with open('./accounts.csv') as file:
        csv_reader=csv.reader(file)
        accounts = [row for row in csv_reader]
    return accounts

# Add row to .csv *****
def add_account(csv_data: list, new_account: list):
    with open('./accounts.csv', 'w',newline="") as file:
        csv_writer=csv.writer(file)
        csv_data.append(new_account)

        for acc in csv_data:
            csv_writer.writerow(acc)

# Delete row from .csv ******
def delete_account(accounts: list, account_index: int):
    with open('./accounts.csv', 'w',newline="") as file:
        csv_writer=csv.writer(file)
        accounts.pop(account_index)

        for acc in accounts:
            csv_writer.writerow(acc)

# Update row in .csv ******
def update_account(accounts: list, updated_account: list, account_index: int):
    with open('./accounts.csv', 'w',newline="") as file:
        csv_writer=csv.writer(file)
        accounts.pop(account_index)
        accounts.insert(account_index, updated_account)

        for acc in accounts:
            csv_writer.writerow(acc)

def check_if_bank_exists():
    # Specify the file path
    file_path = './accounts.csv'

    # Check if the file exists
    if os.path.exists(file_path):
        return True
    else:
        return False
 
# AUTHENTICATION      
###################################################

# Validate credentials
def validate_credentials(username: str, password: str, accounts: list):
    account = find_account_by_username(accounts, username)

    if account != None:
        if account[4] == password:
            return True
    
    return False

# Check if account number exists
# def check_if_account_exists(accounts: list, account_number: int):
#     for account in accounts:
#         print(account)
#         if account[0] == str(account_number):
#             return True
#     return False

# Find account my username
def find_account_by_username(accounts: list, username: str):
    if len(accounts) != 0:
        for account in accounts:
            if account[3] == username:
                return account
    else: 
        return None
    
# MENU EXECUTION
###################################################
def execute_login_menu(accounts: list):
    valid_credentials = False
    while valid_credentials != True:
        print('LOGIN MENU')
        username = input('Username?: ')
        password = input('Password?: ')

        valid_credentials = validate_credentials(username, password, accounts)
        if valid_credentials == False:
            print('Invalid username or password. Please try again.\n')
        else: 
            print('Login Success!\n')
            return (username, password)

def execute_user_menu(current_account: Account, all_accounts):
    user_account = current_account
    accounts = all_accounts

    command = -1
    while command != '5':
        print('USER MENU')
        print('1. Show Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Transfer')
        print('5. Logout\n')
        command = input('Please enter a command: ')
        print()

        if command == '1':
            user_account.display_account()
       
        elif command == '2':
            amount = input('Please enter an amount (ex. 100.00): ')
            if re.match(r'^-?\d+(?:\.\d+)$', amount) is not None:
                success = accounts.deposit(user_account.account_num, float(amount))
                if success:
                    print('Deposit completed.\n')
                else:
                    print('Deposit failed.\n')
            else:
                print('Must be a dollar amount.\n')
       
        elif command == '3':
            amount = input('Please enter an amount (ex. 100.00): ')
            if re.match(r'^-?\d+(?:\.\d+)$', amount) is not None:
                success = accounts.withdraw(user_account.account_num, float(amount))
                if success:
                    print('Withdraw completed.\n')
                else:
                    print('Withdraw failed. Insufficient Funds.\n')
            else:
                print('Must be a dollar amount.\n')
       
        elif command == '4':
            tranferee = input('Please enter the account number to transfer to: ')
            amount = input('Please enter an amount (ex. 100.00): ')
            if re.match(r'^-?\d+(?:\.\d+)$', amount) is not None:
                success = accounts.transfer(user_account.account_num, tranferee, float(amount))
                if success:
                    print('Transfer completed.\n')
                else:
                    print('Transfer failed.\n')
            else:
                print('Must be a dollar amount.\n')
       
        elif command == '5':
            print('Returning to Login Screen\n')
       
        else:
            print('Invalid Command.\n')



    
 






