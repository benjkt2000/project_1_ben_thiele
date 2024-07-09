class Account:
    def __init__(self, row_data):
        self.account_num = row_data[0]
        self.first_name = row_data[1]
        self.last_name = row_data[2]
        self.username = row_data[3]
        self.password = row_data[4]
        self.balance = row_data[5]

    def display_account(self):
        print('Name: ' + self.first_name + ' ' + self.last_name)
        print('User name: ' + self.username)
        print('Account Number: ' + self.account_num)
        print('Balance: ' + self.balance + '\n')