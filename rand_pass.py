import secrets 

global length
global password

def pass_requirements(password):
    
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

def rand_pass(length):

    char_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    password_found = False
    
    while not password_found:
        try: 
            if length < 14 or length > 128 or length == "":
                print("Please enter a number between 14 and 128")
                length = int(input("Enter the length of your password: "))
            else:
                password = ''.join((secrets.choice(char_set) for _ in range(length)))
                if pass_requirements(password):
                    password_found = True
        except ValueError as e:
            print(e)
            length = int(input("Enter the length of your password: "))
    return password

def main():
    length = int(input("Enter the length of your password: "))
    password = rand_pass(length)
    print(f"Your password is: {password}")
    
main()

        

