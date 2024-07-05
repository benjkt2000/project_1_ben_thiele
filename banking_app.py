import csv
# READ/WRITE FUNCTIONS
###################################################

# Open .csv and retrieve rows
def retrieve_accounts():
    with open('./accounts2.csv') as file:
        csv_reader=csv.reader(file)
        accounts = [row for row in csv_reader]
    return accounts

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

# BANKING/VALIDATION FUNCTIONS       
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



######################################################
accounts = retrieve_accounts()
# print(accounts)

account = accounts[1]
# print(account)

#index = find_account_index(accounts, account)
#print(index)

# new_account = [1,'ben', 'thiele' , 'bthiele', 'pass', '100']
# update_account(accounts, new_account, index)

# retrieved_account = find_account_by_username(accounts, "bthiele")
# print(retrieved_account)

# print(validate_credentials('bthiele', 'pass', accounts))







