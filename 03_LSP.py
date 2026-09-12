class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False


class WithdrawableAccount(Account):

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False

        self.balance -= amount
        return True


class SavingsAccount(WithdrawableAccount):

    def withdraw(self, amount):
        print("Savings account withdrawal")
        return super().withdraw(amount)


class CurrentAccount(WithdrawableAccount):

    def withdraw(self, amount):
        print("Current account withdrawal")
        return super().withdraw(amount)


class FixedDepositAccount(Account):
    """
    Fixed Deposit does not inherit from WithdrawableAccount
    because withdrawal is not supported.
    """

    def withdraw(self, amount):
        raise Exception("Withdrawal is impossible")


# Demonstration

savings = SavingsAccount("Ravi", 5000)
current = CurrentAccount("Arun", 10000)
fixed_deposit = FixedDepositAccount("Kumar", 50000)

print("Savings withdrawal:", savings.withdraw(1000))
print("Savings balance:", savings.balance)

print("Current withdrawal:", current.withdraw(2000))
print("Current balance:", current.balance)

try:
    fixed_deposit.withdraw(1000)
except Exception as e:
    print("Fixed Deposit:", e)