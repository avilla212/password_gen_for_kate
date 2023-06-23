import secrets
import pandas as pd
import os
import time 

def sleep_time():
    print("...")
    time.sleep(1.5)

# Function to check if the password meets the requirements
def pass_requirements(password):
    
    # Flag variables to check if the password has at least one of each requirement
    has_lower = False
    has_upper = False
    has_special = False
    has_number = False

    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_number = True
        else:
            has_special = True

    if not (has_lower and has_upper and has_special and has_number):
        return False

    return True


def generate_password(amount, length):
    # Flag variables to check if the user input is valid
    correct_amount = False
    correct_length = False

    # Validate user input amount
    while not correct_amount:
        try:
            amount = int(input("How many passwords would you like to generate? (Enter 1-14): "))
            if amount < 1 or amount > 14:
                print("\nPlease enter a number between 1 and 14")
            else:
                correct_amount = True
        except ValueError as e:
            print(e)

    # Validate user input length
    while not correct_length:
        try:
            length = int(input("Enter the length of your password (Enter 13-128): "))
            if length < 13 or length > 128:
                print("\nPlease enter a number between 13 and 128")
            else:
                correct_length = True
        except ValueError as e:
            print(e)

    # List to store the passwords
    passwords = []

    # Generate the passwords
    for _ in range(amount):
        # Flag variable to check if the password meets the requirements
        password_found = False
        while not password_found:
            try:
                password = rand_pass(length)
                if pass_requirements(password):
                    passwords.append(password)
                    password_found = True
            except ValueError as e:
                print(e)

    return passwords

# Function to generate the password
def rand_pass(length):
    
    char_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    password = "".join(secrets.choice(char_set) for _ in range(length))
    return password

# Function to save the passwords to a file
def save_to_file(passwords):
    answer = input("Would you like to save your passwords to a file? (y/n): ")

    # Validate user input
    while answer.lower() != "y" and answer.lower() != "n":
        answer = input("Please enter 'y' or 'n': ")

    if answer.lower() == "n":
        print_passwords(passwords)
        return

    if answer.lower() == "y":
        print("What operating system are you using?")
        print("1. Windows")
        print("2. Mac")

        # Flag variable to check if the user input is valid
        os_flag = False
        while not os_flag:
            try:
                os_choice = int(input("Enter the number corresponding to your operating system: "))
                if os_choice in [1, 2]:
                    os_flag = True
                else:
                    print("Invalid input. Please enter '1' for Windows or '2' for Mac.")
            except ValueError:
                print("Invalid input. Please enter '1' for Windows or '2' for Mac.")

        if os_choice == 1:
            save_to_windows(passwords)

        elif os_choice == 2:
            save_to_mac(passwords)

# Function to save the passwords to a Windows file
def save_to_windows(passwords):
    # Flag variable to check if the user input is valid
    os_name = "Windows"
    
    # Get the desktop path
    desktop_path = os.path.expanduser("~\Desktop")

    folder_flag = False
    while not folder_flag:
        try:
            folder_name = input("Enter the folder name (leave blank for the desktop): ")
            # If the user enters a folder name, create the folder
            if folder_name:
                folder_path = os.path.join(desktop_path, folder_name)
                os.makedirs(folder_path, exist_ok=True)
                folder_flag = True
            else:
                folder_flag = True
        except ValueError:
            print("Invalid folder name. Please try again.")

    file_flag = False
    while not file_flag:
        try:
            # Get the file name
            file_name = input("Enter the file name(Include file type - .txt,.csv and etc ...): ")
            file_path = os.path.join(folder_path if folder_name else desktop_path, file_name)
            file_flag = True
        except ValueError:
            print("Invalid file name. Please try again.")
    try:
        # Write the passwords to the file
        with open(file_path, "w") as file:
            file.write("\n".join(passwords))
        print(f"Passwords saved to {os_name} file path: {file_path}")
    except OSError as e:
        print(f"Error occurred while saving passwords: {str(e)}")

# Function to save the passwords to a Mac file
def save_to_mac(passwords):
    os_name = "Mac"

    folder_flag = False
    # Get the Documents path
    while not folder_flag:
        try:
            # Get the folder name
            folder_name = input("Enter the folder name (leave blank for desktop): ")
            if folder_name:
                folder_path = os.path.expanduser("~/Documents/" + folder_name)
                os.makedirs(folder_path, exist_ok=True)
                folder_flag = True
            else:
                folder_flag = True
        
        except ValueError:
            print("Invalid folder name. Please try again.")

    file_flag = False
    # Get the file name
    while not file_flag:
        try:
            # Get the file name
            file_name = input("Enter the file name(Include file type - .txt,.csv and etc ...): ")
            file_path = os.path.join(folder_path, file_name)
            file_flag = True
        except ValueError:
            print("Invalid file name. Please try again.")

    try:
        # Write the passwords to the file
        with open(file_path, "w") as file:
            file.write("\n".join(passwords))
        print(f"Passwords saved to {os_name} file path: {file_path}")
    except OSError as e:
        print(f"Error occurred while saving passwords: {str(e)}")


# Function to print the passwords to the console
def print_passwords(passwords):
    
    df = pd.DataFrame(passwords, columns=[""])
    df.index = range(1, len(df) + 1)
    print("\nHere are your passwords: ")
    df.to_string(index=True, justify="right")
    print(df)

def main():
    
    passwords = generate_password(0, 0)
    save_to_file(passwords)

main()


# IMPORTANT: Work on welcome menu first. Then work on the TODO list.

# TODO:
# - Add functionality to allow the user to create a folder and/or file name if needed.
# - Check if the folder and/or file name already exist.
#     - If the folder name exists, ask the user if they want to overwrite the folder.
#         - If not, prompt the user to enter a new folder name.
#     - If the file name exists, ask the user if they want to overwrite the file.
#         - If not, prompt the user to enter a new file name.
# - Implement the above steps for both Mac and Windows operating systems.
# - Integrate the functionality into a GUI using Next.js and Tailwind CSS.
