from abc import ABC,abstractmethod

class Depositable(ABC):
    @abstractmethod
    def deposit(self,amount):
        pass


class Withdrawable(ABC):
    @abstractmethod
    def withdraw(self,amount):
        pass


class Transferable(ABC):
    @abstractmethod
    def transfer(self,amount):
        pass


class StatementProvider(ABC):
    @abstractmethod
    def generate_statement(self):
        pass


class SavingsAccount(Depositable,Withdrawable,Transferable):
    def __init__(self,balance=0):
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            return True
        return False

    def withdraw(self,amount):
        if amount<=0 or amount>self.balance:
            return False

        self.balance-=amount
        return True

    def transfer(self,amount):
        if amount<=0 or amount>self.balance:
            return False

        self.balance-=amount
        return True


class FixedDepositAccount(Depositable):
    def __init__(self,balance=0):
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            return True
        return False


savings=SavingsAccount(10000)

print("Deposit:",savings.deposit(2000))
print("Balance:",savings.balance)

print("Withdraw:",savings.withdraw(1000))
print("Balance:",savings.balance)

fixed_deposit=FixedDepositAccount(50000)

print("Fixed Deposit:",fixed_deposit.deposit(5000))
print("Fixed Deposit Balance:",fixed_deposit.balance)