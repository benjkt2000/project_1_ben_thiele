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
run_app = True
while run_app:

    credentials = execute_login_menu(csv_data)
    current_user_account = Account(find_account_by_username(csv_data, credentials[0]))

    if current_user_account.username == 'admin':
        print(f'Logged in as {credentials[0]}\n')
        run_app = execute_admin_menu(current_user_account, accounts)
    else:
        print(f'Logged in as {credentials[0]}\n')
        run_app = execute_user_menu(current_user_account, accounts)


