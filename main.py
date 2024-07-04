from bankaccount import BankAccount

# Instantiate 3 instances of bank accounts
account1 = BankAccount("1234567", "Alexander", 1000)
account2 = BankAccount("2345678", "Barbara", 1500)
account3 = BankAccount("3456789", "Charlie", 200)

# Performing actions on account1
account1.display_account_info() # Should print Account Number: 1234567, Account Holder Name: Alexander, Current Balance $1000
account1.deposit(1200)
account1.withdraw(500)
account1.get_balance()  # Should print $1700.0


# Performing actions on account2
account2.display_account_info() # Should print Account Number: 2345678, Account Holder Name: Barbara, Current Balance $1500
account2.deposit(-200) # Should print Please enter a number greater than 0 to deposit
account2.withdraw(-150) # Should Please enter a number greater than 0 to withdraw
account2.get_balance() # Should return $1500

# Performing actions on account3
account3.display_account_info() # Should print Account Number: 3456789, Account Holder Name: Charlie, Current Balance $200
account3.withdraw(300) # Should print Insufficient amount to withdraw. You currently have $200 in your account
account3.withdraw("fifty") # Should print Please enter a numerical amount to withdraw
account3.deposit("100") # Should be successful with no error messages
account3.get_balance() # Should be $300.0