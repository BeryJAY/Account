import sys
class BankAccount(object): 
    
    def __init__(self):
        self.balance=100000
        self.active = True
        
    def open_account(self,name):
        self.name=name
        return self.name   
    
    def deposit(self,amount):
        self.balance += amount
        return self.balance

    def withdraw(self,amount):
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance
    def close_account(self):
        result=self.active
        return result
    
    
