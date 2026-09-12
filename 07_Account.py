from abc import ABC, abstractmethod


class Account(ABC):

    def __init__(
        self,
        account_number: int,
        name: str,
        age: int,
        initial_balance: float
    ) -> None:

        self._account_number = account_number
        self._name = name

        # Minimum age is 18
        self._age = max(age, 18)

        # Initial balance cannot be below minimum balance
        self._balance = max(
            initial_balance,
            self.minimum_balance
        )

        self._status = "Active"
        self._pin = None

    @property
    @abstractmethod
    def minimum_balance(self) -> float:
        pass

    @property
    def account_number(self) -> int:
        return self._account_number

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def status(self) -> str:
        return self._status

    def deposit(self, amount: float) -> bool:

        if self._status != "Active":
            return False

        if amount <= 0:
            return False

        self._balance += amount

        return True

    def withdraw(
        self,
        amount: float,
        pin: int | None = None
    ) -> bool:

        if self._status != "Active":
            return False

        if self._pin is not None:

            if pin is None or pin != self._pin:
                return False

        if amount <= 0:
            return False

        if self._balance - amount < self.minimum_balance:
            return False

        self._balance -= amount

        return True

    def close_account(self) -> bool:

        if self._status == "Inactive":
            return False

        self._status = "Inactive"

        return True

    def reopen_account(self) -> bool:

        if self._status == "Active":
            return False

        self._status = "Active"

        return True

    def set_pin(self, pin: int) -> bool:

        if 1000 <= pin <= 9999:
            self._pin = pin
            return True

        return False

    def verify_pin(self, pin: int) -> bool:

        return self._pin is not None and self._pin == pin

    def has_pin(self) -> bool:

        return self._pin is not None


class SavingsAccount(Account):

    @property
    def minimum_balance(self) -> float:
        return 500.0


class CurrentAccount(Account):

    @property
    def minimum_balance(self) -> float:
        return 1000.0


# ------------------------------------------------
# Demonstration
# ------------------------------------------------

account = SavingsAccount(
    101,
    "Ravi",
    17,
    200
)

print("Account Number:", account.account_number)
print("Name:", account.name)

# 17 becomes 18
print("Age:", account.age)

# 200 becomes 500 because of minimum balance
print("Initial Balance:", account.balance)

print("Status:", account.status)


print("\nDeposit Rs. 1000:")
print(account.deposit(1000))

print("Balance:", account.balance)


print("\nSet PIN 1234:")
print(account.set_pin(1234))


print("\nWithdraw Rs. 500 with correct PIN:")
print(account.withdraw(500, 1234))

print("Balance:", account.balance)


print("\nWithdraw Rs. 500 with wrong PIN:")
print(account.withdraw(500, 9999))

print("Balance:", account.balance)


print("\nClose Account:")
print(account.close_account())

print("Deposit after closing:")
print(account.deposit(100))

print("\nReopen Account:")
print(account.reopen_account())

print("Deposit after reopening:")
print(account.deposit(100))

print("Final Balance:", account.balance)