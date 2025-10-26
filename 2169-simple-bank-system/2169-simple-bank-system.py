class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.balance = balance
        

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        if not self.isValidAccount(account1):
            return False
        
        if not self.isValidAccount(account2):
            return False

        if self.balance[account1 - 1] < money:
            return False
        
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if not self.isValidAccount(account):
            return False

        self.balance[account - 1] += money
        return True
        

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if not self.isValidAccount(account):
            return False
        if self.balance[account - 1] < money:
            return False
        
        self.balance[account - 1] -= money
        return True
        
    def isValidAccount(self, account):
        if account < 1 or account > len(self.balance):
            return False
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)