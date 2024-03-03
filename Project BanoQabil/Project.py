import time
import getpass

# Dictionary to store user accounts
accounts = {}

# Function to create a new account
def create_account():
    username = input("Enter a username: ")
    if username in accounts:
        print("Username already exists!")
        return
    password = getpass.getpass("Enter a password: ")
    confirm_password = getpass.getpass("Confirm your password: ")
    if password != confirm_password:
        print("Passwords do not match!")
        return
    accounts[username] = password
    print("Account created successfully!")

# Function to test an account
def test_account():
    username = input("Enter your username: ")
    if username not in accounts:
        print("Username does not exist!")
        return
    password = getpass.getpass("Enter your password: ")
    if accounts[username] != password:
        print("Incorrect password!")
        return
    f = open("budget.txt", "r")
    print(f.read())


# Initialize the failed attempts dictionary
failed_attempts = {}

# Function to handle login attempts
def handle_login_attempts(username):
    if username in failed_attempts:
        failed_attempts[username] += 1
        if failed_attempts[username] > 5:
            print("Access denied! Account locked.")
            del failed_attempts[username]
            return True
        else:
            print("Access denied!")
            return False
    else:
        failed_attempts[username] = 1
        print("Access denied!")
        return False

# Main function
def main():
    while True:
        print("\n1. Create account")
        print("2. Login")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_account()
        elif choice == 2:
            username = input("Enter your username: ")
            if handle_login_attempts(username):
                continue
            test_account()
        elif choice == 3:
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()