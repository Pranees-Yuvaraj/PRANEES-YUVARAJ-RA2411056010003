class BankAccount:
    def __init__(self,account_number,name,balance=0):
        self.account_number=account_number
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        if amount<=0:
            return False
        self.balance+=amount
        return True

    def withdraw(self,amount):
        if amount<=0 or amount>self.balance:
            return False
        self.balance-=amount
        return True


class AccountRepository:
    def save(self,account):
        print(f"Saving account {account.account_number} to database")


class NotificationService:
    def send(self,message):
        print(f"Sending notification: {message}")


class StatementGenerator:
    def generate(self,account):
        return (
            f"Statement for Account: {account.account_number}\n"
            f"Name: {account.name}\n"
            f"Balance: Rs. {account.balance}"
        )


class TaxCalculator:
    def calculate(self,balance):
        return balance*0.10


account=BankAccount(101,"Ravi",5000)

account.deposit(1000)
account.withdraw(500)

repository=AccountRepository()
repository.save(account)

notification=NotificationService()
notification.send("Transaction completed successfully")

statement=StatementGenerator()
print(statement.generate(account))

tax=TaxCalculator()
print("Tax:",tax.calculate(account.balance))