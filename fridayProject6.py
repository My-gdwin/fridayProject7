# Define a class for BankAccount
class BankAccount:
    def __init__(self, account_number, balance=0):
        """
        Initialize the BankAccount with an account number and a starting balance (default is 0).
        """
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """
        Method to deposit money into the account.
        The balance is increased by the deposit amount.
        """
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Method to withdraw money from the account.
        The balance is decreased by the withdrawal amount if there are sufficient funds.
        """
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"${amount} withdrawn successfully.")
            else:
                print("Insufficient funds for withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        """
        Method to check and display the current balance.
        """
        print(f"Your current balance is: ${self.balance}")

# Main function to interact with the bank account
def main():
    # Create an instance (account) for the user with account number 12345 and an initial balance of 0
    account = BankAccount(12345)

    # Greet the user
    print("Welcome to the Bank Account Manager!")
    
    while True:
        # Ask for the user's account number
        input_account_number = int(input("\nPlease enter your account number (or 0 to exit): "))

        # Check if the input account number matches the created account
        if input_account_number == account.account_number:
            print("\nOptions: ")
            print("1. Deposit money")
            print("2. Withdraw money")
            print("3. Check balance")
            print("4. Exit")

            # Ask the user to choose an option
            option = int(input("Choose an option (1-4): "))

            if option == 1:
                # Deposit money
                deposit_amount = float(input("Enter amount to deposit: $"))
                account.deposit(deposit_amount)
            elif option == 2:
                # Withdraw money
                withdraw_amount = float(input("Enter amount to withdraw: $"))
                account.withdraw(withdraw_amount)
            elif option == 3:
                # Check balance
                account.check_balance()
            elif option == 4:
                # Exit the program
                print("Thank you for using the Bank Account Manager. Goodbye!")
                break
            else:
                print("Invalid option. Please choose a number between 1 and 4.")
        elif input_account_number == 0:
            # Exit if the user enters 0
            print("Thank you for using the Bank Account Manager. Goodbye!")
            break
        else:
            # Handle incorrect account number input
            print("Invalid account number. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
