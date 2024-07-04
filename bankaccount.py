# creating a class called BankAccount
class BankAccount:

    # Initializing attributes of account_number, account_holder, and initial_balance
    def __init__(self, account_number, account_holder, initial_balance):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__initial_balance = initial_balance
        self.__current_balance = initial_balance

    # Function for depositing money
    def deposit(self, amount):
        try:
            if float(amount) > 0:
                self.__current_balance += float(amount)
                return self.__current_balance
            else:
                print("Please enter a number greater than 0 to deposit")
        except ValueError:
            print("Please enter a numerical amount to deposit")

    # Function for withdrawing money
    def withdraw(self, amount):
        try:
            if float(amount) > 0 and float(amount) <= self.__current_balance:
                self.__current_balance -= float(amount)
                return self.__current_balance
            elif float(amount) <= 0:
                print("Please enter a number greater than 0 to withdraw")
            else:
                print(f'Insufficient amount to withdraw. You currently have ${self.__current_balance} in your account')
        except ValueError:
            print("Please enter a numerical amount to withdraw")

    # Function for getting current balance
    def get_balance(self):
        print(f'Current balance: ${self.__current_balance}')
    
    # Function for displaying account info (account number, account holder name, and current balance)
    def display_account_info(self):
        print (f'Account Number: {self.__account_number} \nAccount Holder Name: {self.__account_holder} \nCurrent Balance: ${self.__current_balance}')

