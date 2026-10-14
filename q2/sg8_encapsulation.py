class BankAccount:
    def __init__(self, account_number: int, balance: float):
        self.__account_number = account_number
        self.__balance = 0
        self.set_account_number(account_number)
        self.set_balance(balance)
        self.get_account_number()
        self.get_balance()
#initializes the class BankAccount
  
    def set_account_number(self, account_number: int):
        if isinstance(account_number, int) and account_number > 0:
            self.__account_number = account_number
        else:
            raise ValueError("Account number must be a positive integer.")
#ensures that the account_number is a positive integer.

    def set_balance(self, balance: float):
        if isinstance(balance, (int, float)) and balance >= 0:
            self.__balance = balance
        else:
            raise ValueError("The balance must not be a negative number.")
#ensures that the balance is a positive integer.

    def get_bank_account(self, bank_account):
        other_value = other.__account_number if isinstance(other, BankAccount) else int(other)
        return self.__account_number == other_value
#returns vlue for bank_account.
    def get_balance(self):
        return self.__balance  
#returns value for balance.

a1 = int(input("Account "))
a1 = BankAccount(int(input("Account Number: ")), float(input("Balance: ")))

print(a1.get_account_number())
print(a1.get_balance())

a1.set_account_number(int(input("Account Number: ")))
a1.set_balance(float(input("Balance: ")))

print(a1.get_account_number())
print(a1.get_balance())

#asks for user input and stores it.
#di ko natapos sir, and di gumagana, ewan q kung bakit:(
