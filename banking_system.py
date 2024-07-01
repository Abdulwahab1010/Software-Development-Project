# Function to initialize a new account with a starting balance of zero
def initialize_account():
    return 0.0

# Function to display the menu options
def display_menu():
    print("\nWelcome to the Basic Banking System")
    print("Please choose an option:")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")

# Function to handle deposits
def deposit(balance):
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Amount must be a positive number.")
        else:
            balance += amount
            print(f"Successfully deposited ${amount:.2f}. New balance is ${balance:.2f}.")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")
    return balance

# Function to handle withdrawals
def withdraw(balance):
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Amount must be a positive number.")
        elif amount > balance:
            print("Insufficient funds. Cannot withdraw more than the current balance.")
        else:
            balance -= amount
            print(f"Successfully withdrew ${amount:.2f}. New balance is ${balance:.2f}.")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")
    return balance

# Function to check current balance
def check_balance(balance):
    print(f"Your current balance is ${balance:.2f}.")

# Main function to run the banking system
def main():
    balance = initialize_account()
    
    while True:
        display_menu()
        
        try:
            choice = int(input("Enter your choice (1-4): "))
            
            if choice == 1:
                balance = deposit(balance)
            elif choice == 2:
                balance = withdraw(balance)
            elif choice == 3:
                check_balance(balance)
            elif choice == 4:
                print("Exiting the program. Thank you for using the Basic Banking System.")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a numerical value corresponding to the menu options.")

# Run the banking system
if __name__ == "__main__":
    main()
