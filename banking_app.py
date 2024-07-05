import csv
# READ/WRITE FUNCTIONS
###################################################

# Open .csv and retrieve rows
def retrieve_accounts():
    with open('./accounts2.csv') as file:
        csv_reader=csv.reader(file)
        accounts = [row for row in csv_reader]
    return accounts

# Add row to .csv
def add_account(accounts: list, new_account: list):
    with open('./accounts2.csv', 'w',newline="") as file:
        csv_writer=csv.writer(file)
        accounts.append(new_account)

        for acc in accounts:
            csv_writer.writerow(acc)

# Update row in .csv
# Add account validation?
def update_account(accounts: list, updated_account: list, account_index: int):
    with open('./accounts2.csv', 'w',newline="") as file:
        csv_writer=csv.writer(file)
        accounts.pop(account_index)
        accounts.insert(account_index, updated_account)

        for acc in accounts:
            csv_writer.writerow(acc)

# Find index of account
# make sure list is not empty, or if index is out of bounds, maybe use a find account by index method 
def find_account_index(accounts: list, account: list):
    account_index = accounts.index(account)
    return account_index

# Find account my username
def find_account_by_username(accounts: list, username: str):
    if len(accounts) != 0:
        for account in accounts:
            if account[3] == username:
                return account
    else: 
        return None

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


# BANK FEATURE METHODS
######################################################
def retrieve_balance(account: list):
    if len(account) == 6:
        return "{:.{}f}".format(float(account[5]), 2)

def deposit(accounts: list, account: list, amount: float, account_index: int):
    updated_account = account

    if len(account) == 6:
        original_balance = retrieve_balance(account)
        updated_account[5] = "{:.{}f}".format(float(amount) + float(original_balance), 2) 
        update_account(accounts, updated_account, account_index)

    return updated_account

def withdraw(accounts: list, account: list, amount: float, account_index: int):
    updated_account = account

    if len(account) == 6:
        original_balance = retrieve_balance(account)
        new_balance = float(original_balance) - amount

        if new_balance > -500.00:
            updated_account[5] = "{:.{}f}".format(float(new_balance), 2)
            update_account(accounts, updated_account, account_index)

    return updated_account    


######################################################
accounts = retrieve_accounts()
# print(accounts)

account = accounts[1]
# print(account)

print(deposit(accounts, account, 157.63, find_account_index(accounts, account)))
#print(withdraw(accounts, account, 116.53, find_account_index(accounts, account)))

# print(retrieve_balance(account))

# index = find_account_index(accounts, account)
# print(index)

#new_account = [4,'Saul' , 'Shields' ,'sshields', 'pass', 100]
#update_account(accounts, new_account, index)

#add_account(accounts, new_account)

# retrieved_account = find_account_by_username(accounts, "bthiele")
# print(retrieved_account)

# print(validate_credentials('bthiele', 'pass', accounts))







