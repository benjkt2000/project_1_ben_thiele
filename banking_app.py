import csv
import os
import pandas as pd
import numpy as np
# CRUD FUNCTIONS
###################################################
# Create default .csv file
def create_bank():
    admin_account = ['000', '', '', 'admin', 'admin', '']
    with open('./accounts.csv', 'w',newline="") as file:
        csv_writer=csv.writer(file)
        csv_writer.writerow(admin_account)

# Open .csv and retrieve rows
def retrieve_accounts():
    with open('./accounts.csv') as file:
        csv_reader=csv.reader(file)
        accounts = [row for row in csv_reader]
    return accounts

# Add row to .csv
def add_account(accounts: list, new_account: list):
    with open('./accounts.csv', 'w',newline="") as file:
        csv_writer=csv.writer(file)
        accounts.append(new_account)

        for acc in accounts:
            csv_writer.writerow(acc)

# Delete row from .csv
def delete_account(accounts: list, account_index: int):
    with open('./accounts.csv', 'w',newline="") as file:
        csv_writer=csv.writer(file)
        accounts.pop(account_index)

        for acc in accounts:
            csv_writer.writerow(acc)

# Update row in .csv
# Add account validation?
def update_account(accounts: list, updated_account: list, account_index: int):
    with open('./accounts.csv', 'w',newline="") as file:
        csv_writer=csv.writer(file)
        accounts.pop(account_index)
        accounts.insert(account_index, updated_account)

        for acc in accounts:
            csv_writer.writerow(acc)

# UTILITY FUNCTIONS       
###################################################

# Find index of account
def find_account_index(accounts: list, account: list):
    account_index = accounts.index(account)
    return account_index

# Find account by account number
def find_account_by_account_number(accounts: list, account_num: str):
    if len(accounts) != 0:
        for account in accounts:
            if account[0] == str(account_num):
                return account
    else:
        return None  
    
# Find account my username
def find_account_by_username(accounts: list, username: str):
    if len(accounts) != 0:
        for account in accounts:
            if account[3] == username:
                return account
    else: 
        return None
    
# Print formatted account
def formatted_account_lookup(accounts: list, account_num: str):
    account =  find_account_by_account_number(accounts, account_num)

    if account != None:
        print('Name: ' + account[1] + ' ' + account[2])
        print('User name: ' + account[3])
        print('Account Number: ' + account[0])
        print('Balance: ' + account[5])
        
    else:
        print('account not found')

# Return account balance in correct format
def retrieve_balance(account: list):
    if len(account) == 6:
        return "{:.{}f}".format(float(account[5]), 2)
    
# Deposit money into account
def deposit(accounts: list, account: list, amount: float, account_index: int):
    updated_account = account

    if len(account) == 6:
        original_balance = retrieve_balance(account)
        updated_account[5] = "{:.{}f}".format(float(amount) + float(original_balance), 2) 
        update_account(accounts, updated_account, account_index)

    return updated_account

# Withdraw
# Perhaps move -500.00 check to parent method
def withdraw(accounts: list, account: list, amount: float, account_index: int):
    updated_account = account

    if len(account) == 6:
        original_balance = retrieve_balance(account)
        new_balance = float(original_balance) - amount

        if new_balance > -500.00:
            updated_account[5] = "{:.{}f}".format(float(new_balance), 2)
            update_account(accounts, updated_account, account_index)

    return updated_account 

# VALIDATION FUNCTIONS       
###################################################

# Validate credentials
def validate_credentials(username: str, password: str, accounts: list):
    account = find_account_by_username(accounts, username)

    if account != None:
        if account[4] == password:
            return True
    
    return False

# Check if account number exists
def check_if_account_exists(accounts: list, account_number: int):
    for account in accounts:
        print(account)
        if account[0] == str(account_number):
            return True
    return False

# Validate account format? ex. length, data types, account number does not exist

# def validate_account_format(account: str):
    
#     if len(account) != 6:
#         print("Invalid Length") 
#         return False
#     elif type(account[0]) != int:
#         print('Invalid data type for account')
#         return False
#     elif type(account[1]) != str:
#         print('Invalid data type for first_name')
#         return False
#     elif type(account[2]) != str:
#         print('Invalid data type for last_name')
#         return False
#     elif type(account[3]) != str:
#         print('Invalid data type for user_name')
#         return False
#     elif type(account[4]) != str:
#         print('Invalid data type for password')
#         return False
#     elif type(account[5]) != float:
#         print('Invalid data type for balance')        
    
#     return True

def check_if_bank_exists():
    # Specify the file path
    file_path = './accounts.csv'

    # Check if the file exists
    if os.path.exists(file_path):
        return True
    else:
        return False

# BANK FEATURE METHODS
###################################################### 
def transfer(accounts: list, sending_acc_num: int, receiving_acc_num: int, amount: float):
    sending_acc = find_account_by_account_number(accounts, sending_acc_num)
    receiving_acc = find_account_by_account_number(accounts, receiving_acc_num)

    sending_acc_bal = sending_acc[5]

    if float(sending_acc_bal) - amount < -500.00:
        return sending_acc
    else:
        updated_sender = withdraw(accounts, sending_acc, amount, find_account_index(accounts, sending_acc))
        deposit(accounts, receiving_acc, amount, find_account_index(accounts, receiving_acc))
        return updated_sender
    
def display_all_accounts(accounts: list):
    formatted_accounts = pd.DataFrame(accounts[1::], columns=['Account Number', 'First Name', 'Last Name', 'User Name', 'Password', 'Balance'])
    formatted_accounts.replace({None: np.nan})

    print(formatted_accounts)




    
# Make sure amounts to deposit are not NEGATIVE!!!
######################################################
create_bank()
accounts = retrieve_accounts()
new_accounts = [
['001','Ben','Thiele','bthiele','pass','100.00'],
['002','Jim','Held','jheld','pass','200.00'],
['003','Frank','Sun','fson','pass','300.00'],
['004','Saul','Shields','sshields','pass','400.00']
]

for acc in new_accounts:
    add_account(accounts, acc)

withdraw(accounts, accounts[1], 2.83, 1)



###############################################
#account = accounts[1]
# print(account)

#print(deposit(accounts, account, 99.07, find_account_index(accounts, account)))
#print(withdraw(accounts, account, 116.52, find_account_index(accounts, account)))

# print(retrieve_balance(account))

# index = find_account_index(accounts, account)
# print(index)

#new_account = ['005','Saul' , 'Shields' ,'sshields', 'pass', '400.00']
#update_account(accounts, new_account, index)

#add_account(accounts, new_account)

# retrieved_account = find_account_by_username(accounts, "bthiele")
# print(retrieved_account)

# print(validate_credentials('bthiele', 'pass', accounts))

# print(find_account_by_account_number(accounts, 1))

# print(transfer(accounts, 2, 4, 150.00))

# display_all_accounts(accounts)

# account_lookup(accounts, '01')

# remove_account(accounts, '3')





