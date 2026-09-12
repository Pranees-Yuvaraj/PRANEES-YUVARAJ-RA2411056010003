from abc import ABC, abstractmethod


class AccountRepository(ABC):

    @abstractmethod
    def save(self, account):
        pass

    @abstractmethod
    def find_by_id(self, account_number):
        pass


class MySQLAccountRepository(AccountRepository):

    def __init__(self):
        self.accounts = {}

    def save(self, account):
        self.accounts[account.account_number] = account
        print("Saving to MySQL")

    def find_by_id(self, account_number):
        print("Fetching from MySQL")
        return self.accounts.get(account_number)


class PostgreSQLAccountRepository(AccountRepository):

    def __init__(self):
        self.accounts = {}

    def save(self, account):
        self.accounts[account.account_number] = account
        print("Saving to PostgreSQL")

    def find_by_id(self, account_number):
        print("Fetching from PostgreSQL")
        return self.accounts.get(account_number)


class Bank:
    """
    Bank depends on AccountRepository abstraction,
    not MySQL or PostgreSQL directly.
    """

    def __init__(self, repository: AccountRepository):
        self.repository = repository

    def save_account(self, account):
        self.repository.save(account)

    def find_account(self, account_number):
        return self.repository.find_by_id(account_number)


class Account:

    def __init__(self, account_number, name):
        self.account_number = account_number
        self.name = name


# Using MySQL

mysql_repository = MySQLAccountRepository()
bank = Bank(mysql_repository)

account = Account(101, "Ravi")

bank.save_account(account)

print(bank.find_account(101).name)


print("\nSwitching to PostgreSQL...\n")


# Using PostgreSQL without modifying Bank

postgres_repository = PostgreSQLAccountRepository()
bank = Bank(postgres_repository)

bank.save_account(account)

print(bank.find_account(101).name)