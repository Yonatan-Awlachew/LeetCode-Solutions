class Bank:

    def __init__(self, balance: List[int]):
        self.bank = {}
        for i,money in enumerate(balance,start=1):
            self.bank[i] = money

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 not in self.bank or account2 not in self.bank: return False
        if self.bank[account1]<money: return False
        self.bank[account1]-=money
        self.bank[account2]+=money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account not in self.bank:return False
        self.bank[account]+=money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account not in self.bank or self.bank[account]< money: return False
        self.bank[account]-=money
        return True
        
