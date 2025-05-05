class Checkbook:
    """
    Class description:
    The Checkbook class represents a simple checking account. It allows the user to deposit
    money into the account, withdraw money, and check the balance.

    Attributes:
        balance (float): The current balance of the checkbook, initially set to 0.0.
    """

    def __init__(self):
        """
        Initializes the checkbook with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Method description:
        This method deposits a specified amount of money into the checkbook. The amount is
        added to the current balance.

        Parameters:
            amount (float): The amount to be deposited into the account.

        Returns:
            None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Method description:
        This method withdraws a specified amount of money from the checkbook. If the amount is
        greater than the current balance, the withdrawal is not allowed and an error message is shown.

        Parameters:
            amount (float): The amount to be withdrawn from the account.

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Method description:
        This method prints the current balance of the checkbook.

        Parameters:
            None

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main function description:
    This function provides an interactive command-line interface for the user to interact with
    the Checkbook class. The user can deposit money, withdraw money, check the balance, or exit the program.

    Parameters:
        None

    Returns:
        None
    """
    cb = Checkbook()  # Create a new checkbook instance
    while True:
        # Prompt user for action
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        
        if action.lower() == 'exit':
            break  # Exit the loop if the user types 'exit'
        elif action.lower() == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()  # Display current balance
        else:
            print("Invalid command. Please try again.")  # Handle invalid command

if __name__ == "__main__":
    main()

