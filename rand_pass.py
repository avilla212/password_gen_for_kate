import secrets 

global length 
global password

def rand_pass(length):
    
    password = ""
    char_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"

    # if length is less than 14 or greater than 128, print error message
    # if the user hits enter without entering a value, print error message
    # use try catch to see if the user entered a number
    
    try:
        if length < 14 or length > 128 or length == "":
            print("Please enter a number between 14 and 128")
            length = int(input("Enter the length of the password: "))
            rand_pass(length)
    except ValueError:
        print("Please enter a number between 14 and 128")
        length = int(input("Enter the length of the password: "))
        rand_pass(length)
 
    
def welcome():
    print("Welcome to the Random Password Generator")
    print("Please enter the length of the password you want to generate")

    length = int(input("Enter the length of the password: "))
    rand_pass(length)
    
    print("Your password is: " + rand_pass(length))


    
welcome() 

        
