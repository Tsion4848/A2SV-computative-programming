class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.isValid(account2):
            return False
        return self.withdraw(account1, money) and self.deposit(account2, money)

    def deposit(self, account: int, money: int) -> bool:
        if not self.isValid(account):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.isValid(account):
            return False
        if self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True
    
    def isValid(self, account: int) -> bool:
        return 1 <= account <= len(self.balance)


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)