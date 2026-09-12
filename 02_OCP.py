from abc import ABC,abstractmethod

class InterestPolicy(ABC):
    @abstractmethod
    def calculate(self,balance:float)->float:
        pass


class SavingsInterestPolicy(InterestPolicy):
    def calculate(self,balance:float)->float:
        return balance*0.04


class CurrentInterestPolicy(InterestPolicy):
    def calculate(self,balance:float)->float:
        return balance*0.01


class SalaryInterestPolicy(InterestPolicy):
    def calculate(self,balance:float)->float:
        return balance*0.05


class FixedDepositInterestPolicy(InterestPolicy):
    def calculate(self,balance:float)->float:
        return balance*0.07


balance=10000

savings=SavingsInterestPolicy()
current=CurrentInterestPolicy()
salary=SalaryInterestPolicy()
fixed_deposit=FixedDepositInterestPolicy()

print("Savings Interest:",savings.calculate(balance))
print("Current Interest:",current.calculate(balance))
print("Salary Interest:",salary.calculate(balance))
print("Fixed Deposit Interest:",fixed_deposit.calculate(balance))