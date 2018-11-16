import unittest
from account import BankAccount

class AccountBalanceTestCase(unittest.TestCase):
  def test_account_owner(self):
    self.my_account= BankAccount()
    self.my_account.open_account("berinda")
    self.assertEqual(self.my_account.name,"berinda",msg="not owner")

    
  def test_deposit(self):
    self.my_account=BankAccount()
    self.my_account.deposit(80000)
    self.assertEqual(self.my_account.balance,180000,msg="add more money")

  def test_withdraw(self):
    self.my_account=BankAccount()
    
    self.my_account.withdraw(50000)
    self.assertEqual(self.my_account.balance,50000,msg="amount too big")

  def test_close_account(self):
    self.my_account=BankAccount()
    self.my_account.close_account()
    self.assertEqual(self.my_account.active,True,msg="account is closed")

  
  

if __name__ == '__main__':
    unittest.main()