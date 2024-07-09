from account import Account
from util import *
import pandas as pd

class Accounts:
    csv_data = []
    accounts = []

    def __init__(self, data: list):       
        self.csv_data = data

        for account in self.csv_data:
           self.accounts.append(Account(account)) 

    # BANKING FEATURES
    def display_all_accounts(self):
        formatted_accounts = pd.DataFrame(self.csv_data[1::], columns=['Account Number', 'First Name', 'Last Name', 'User Name', 'Password', 'Balance'])
        formatted_accounts.replace({None: np.nan})

        print(formatted_accounts)

    def account_lookup(self, account_num: str):
        account = self.find_account_by_account_number(account_num)

        if account == None:
            print('Name: ' + account[1] + ' ' + account[2])
            print('User name: ' + account[3])
            print('Account Number: ' + account[0])
            print('Balance: ' + account[5])
            return True
        
        return False
    

    def create_account(self, new_account: Account) :
        converted_account = self.convert_account_to_list(new_account)
        add_account(self.csv_data, converted_account)
        self.refresh_accounts()

        return True

    def delete_account(self, account_num: Account):
        account_index = self.find_account_index_by_number(account_num)
        if account_index != None:
            delete_account(self.csv_data, account_index)
            self.refresh_accounts()
            return True
        
        return False

    def retrieve_balance(self, account: Account):
        return "{:.{}f}".format(float(account.balance), 2)
    
    def deposit(self, account_num: str, amount: float):
        account = self.find_account_by_account_number(account_num)
        account_index = self.find_account_index_by_number(account_num)

        if account != None and account_index != None and amount >= 0:
            original_balance = account[5]
            account[5] = "{:.{}f}".format(float(amount) + float(original_balance), 2)
            update_account(self.csv_data, account, account_index)
            self.refresh_accounts()
            return True
       
        return False
    
    def withdraw(self, account_num: str, amount: float):
        account = self.find_account_by_account_number(account_num)
        account_index = self.find_account_index_by_number(account_num)

        if account != None and account_index != None:
            original_balance = float(account[5])
            new_balance = original_balance - amount

            if new_balance >= -500.00 and amount >= 0:
                account[5] = "{:.{}f}".format(float(new_balance), 2)
                update_account(self.csv_data, account, account_index)
                self.refresh_accounts()
                return True
       
        return False
    
    def transfer(self, sending_acc_num: str, receiving_acc_num: str, amount: float):
        sending_acc = self.find_account_by_account_number(sending_acc_num)
        sending_acc_index = self.find_account_index_by_number(sending_acc_num)
        receiving_acc = self.find_account_by_account_number(receiving_acc_num)
        receiving_acc_index = self.find_account_index_by_number(receiving_acc_num)

        if sending_acc != None and receiving_acc != None and sending_acc_index != None and receiving_acc_index != None:
            potential_balance = float(sending_acc[5]) - amount
            if potential_balance >= -500 and amount >= 0:
                self.withdraw(sending_acc_num, amount)
                self.deposit(receiving_acc_num, amount)
                self.refresh_accounts()
                return True
        return False
    
    # UTILITES
    def convert_account_to_list(self, account: Account):
        converted_account = []
        
        converted_account.append(str(account.account_num))
        converted_account.append(str(account.first_name))
        converted_account.append(str(account.last_name))
        converted_account.append(str(account.username))
        converted_account.append(str(account.password))
        converted_account.append(str(account.balance))

        return converted_account
    
    def refresh_accounts(self):
        self.accounts = []
        for account in self.csv_data:
            self.accounts.append(Account(account)) 

    def find_account_index_by_number(self, acc_num: str):
        for account in self.accounts:
            if account.account_num == str(acc_num):
                return self.accounts.index(account)
            
    def find_account_by_account_number(self, account_num: str):
        if len(self.csv_data) != 0:
            for account in self.csv_data:
                if account[0] == str(account_num):
                    return account
        else:
            return None  
    