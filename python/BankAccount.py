class BankAccount:
    def __init__(self):
        self.balance = 0
        self.print_balance()

    def withdraw(self, amount):
        print("Withdraw: ",amount)
        self.balance -= amount
        self.print_balance() 
        return self.balance

    def deposit(self, amount):
        print("Deposit: ",amount)
        self.balance += amount
        self.print_balance() 
        return self.balance
    
    def print_balance(self):
        print ("Account balance: ",self.balance)
