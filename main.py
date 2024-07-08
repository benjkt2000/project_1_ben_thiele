from account import Account
from accounts import Accounts
from util import *

# MAIN MENU

# Check if .csv exists
if check_if_bank_exists() == False:
    create_bank()

# Load accounts into program
csv_data = retrieve_accounts()

print(csv_data)


# Login Prompt
# execute_login_menu(accounts)










# new_accounts = [
# ['001','Ben','Thiele','bthiele','pass','100.00'],
# ['002','Jim','Held','jheld','pass','200.00'],
# ['003','Frank','Sun','fson','pass','300.00'],
# ['004','Saul','Shields','sshields','pass','400.00']
# ]