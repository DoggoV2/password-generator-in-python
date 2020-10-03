import random
from typing import List, Any, Union

# function that passes an external user password
def pass_in():
    passin = input("Enter password: ")
    acc_in = input("Enter service that you signed you up for: ")
    with open("password.txt", "a") as b:
        b.write(passin+" - "+acc_in+"\n")
    print("Password \"" + passin + "\" for \"" + acc_in+"\n"" service.")


# function that prints out all saved passwords
def pass_out():

    with open("password.txt", "r") as f:
        password = f.read()
    print(password)

# ignore this.
dd = [""]
# ignore this.

# function that generates passwords
def passgen():

    dd = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'a', 'b', 'c', 'D', 'E', 'F', 'd', 'e'
        , 'e', 'f', 'G', 'H', 'I', 'g', 'h', 'i', 'Q', 'E', 'L', 'J', 'B', 's'
        , 'q', 'w', 'e', 'B', 'C', '#', '@', '!', '&', '@', 'x', 'z', '1', '2', '#', '@', 'a', 'A', 'v', 'h', 'd', 'f', 'g', 'g', 'l', 'd', 'Z', 'q', 'f']


# asking user for length
    choice1 = input("Do you want to specify the length of your password (Y/N): ").lower()
    length = 12
    if choice1 == "y":
        length=int(input("Specify lengh: "))
    if choice1 == "n":
        print("Default is 12 characters.")


# generating password and storing it in a variable, then printing it for the user
    limit = 0
    bb = ''
    while limit < length:
        bb += random.choice(dd)
        limit += 1
    print(bb)

# saving password to file
    choice = input("Do you want to save the password (Y/N): ")

    if choice == "y":
        account = input("What service are you signing up for: ")
        print("Saving file...")
        with open("password.txt", "a") as p:
            p.write(bb+" - "+account+"\n")

    else:
        print("Your password won't be saved to passwords.txt")


# 2 options for user to choose from
def menu():
    opt = input("Welcome. Please choose from the following options:\n1) Generate password\n2) Print out passwords\n3) Save external password\n:: ").lower()

# checking for user input
    if (opt == "1") or (opt == "generate password") or (opt == "generate"):
        print("Your password will be generated shortly...")
        passgen()
    if ((opt == "2") or (opt == "print") or (opt == "print out") or
            (opt == "passwords") or (opt == "print out passwords")):
        print("Printing out passwords...")
        pass_out()

    if (opt == "3") or (opt == "save") or (opt == "save external password"):
        print("Loading function...")
        pass_in()

menu()
