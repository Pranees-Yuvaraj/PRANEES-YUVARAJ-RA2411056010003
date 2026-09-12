from BankAccount import BankAccount
def main():

    account = BankAccount(
        101,
        "Ravi",
        17,
        200,
        "Savings"
    )
    account.set_pin(1234)
    account.deposit(1000)
    account.withdraw(500, 1234)
    account.withdraw(500, 9999)
    account.print_statement()

    print(
        "Interest earned: Rs. "
        + str(account.calculate_interest())
    )
if __name__ == "__main__":
    main()