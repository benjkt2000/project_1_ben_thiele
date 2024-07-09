from account import Account
from accounts import Accounts
from util import *

# BANK APPLICATION

# Check if .csv exists
if check_if_bank_exists() == False:
    create_bank()

# Load accounts into program
csv_data = retrieve_accounts()
accounts = Accounts(csv_data)

# Login Prompt
while True:

    credentials = execute_login_menu(csv_data)
    current_user_account = Account(find_account_by_username(csv_data, credentials[0]))

    if current_user_account.username == 'admin':
        print('logged in as admin')
    else:
        print(f'Logged in as {credentials[0]}\n')
        execute_user_menu(current_user_account, accounts)





# new_accounts = [
# ['001','Ben','Thiele','bthiele','pass','100.00'],
# ['002','Jim','Held','jheld','pass','200.00'],
# ['003','Frank','Sun','fson','pass','300.00'],
# ['004','Saul','Shields','sshields','pass','400.00']
# ]