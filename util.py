import csv
import os
import pandas as pd
import numpy as np

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
def check_if_account_exists(accounts: list, account_number: int):
    for account in accounts:
        print(account)
        if account[0] == str(account_number):
            return True
    return False

# Find account my username
def find_account_by_username(accounts: list, username: str):
    if len(accounts) != 0:
        for account in accounts:
            if account[3] == username:
                return account
    else: 
        return None
    
# MENU EXECUTION
def execute_login_menu(accounts: list):
    valid_credentials = False
    while valid_credentials != True:
        print("LOGIN MENU")
        username = input("Username?: ")
        password = input("Password?: ")

        valid_credentials = validate_credentials(username, password, accounts)
        if valid_credentials == False:
            print("Invalid username or password. Please try again.\n")
        else: print("Login Success!\n")

 






