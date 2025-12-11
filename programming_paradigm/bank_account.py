class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with a starting balance (default 0)."""
        self._account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        if amount > 0:
            self._account_balance += amount
            return True
        return False  # Invalid deposit amount

    def withdraw(self, amount):
        """Withdraw the specified amount if sufficient funds exist."""
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            return True
        return False  # Insufficient funds or invalid amount

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self._account_balance}")
