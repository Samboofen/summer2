class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be greater than zero.")
    
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds. Withdrawal canceled.")
        else:
            print("Withdrawal amount must be greater than zero.")

if __name__ == "__main__":
    account = BankAccount("John Doe", 100.0)
    
    account.deposit(50.0)     
    account.withdraw(30.0) 
    account.withdraw(150.0)   
    account.deposit(100.0)    
    account.withdraw(120.0)   
    print(f"Final balance for {account.owner}: ${account.balance:.2f}")