import random

# This is my first script, i didn't use google or any help so it might be messy.


# fucntion that passes an external user password
def pass_in():
    passin = input("Enter password: ")
    acc_in = input("Enter service that you signed you up for: ")
    with open("password.txt", "a") as b:
        b.write(passin+" - "+acc_in)
        b.close()
    print("Password \""+ passin +"\" for \""+ acc_in+" service.")


# function that prints out all saved passwords
def pass_out():
    with open("password.txt", "r") as f:
      password = f.read()
    print(password)
    f.close()

# function that generates passwords
def passgen():

    # Random lists of characters for the script to choose from
    dd1= ['D', 'Q', 'B', '#', '$', '2', '@', '^', '1', '%','N', 'E', 'N', 'E', 'G','!', '?', 'V', "V", "E", "R", "W", "E", "A", "W", "E", "R", "T", "Y", "K", "X", "Z", "A", "",'x','z', 'a', 's', 'u', 'y', 't', 'r', 'e', 'w', 'q', 'f', 'g', 'e', 'd', 'c', 'c', 'b', 'e', 'a', '3', '2', '@', '@', '%', '&', '4', '4', '2', '1']
    dd2= ['D', 'Q', 'B', '#', '$', '2', '@', '^', '1', '%','N', 'E', 'N', 'E', 'G','!', '?', 'V', "V", "E", "R", "W", "E", "A", "W", "E", "R", "T", "Y", "K", "X", "Z", "A", "",'x','z', 'a', 's', 'u', 'y', 't', 'r', 'e', 'w', 'q', 'f', 'g', 'e', 'd', 'c', 'c', 'b', 'e', 'a', '3', '2', '@', '@', '%', '&', '4', '4', '2', '1']
    dd3= ['D', 'Q', 'B', '#', '$', '2', '@', '^', '1', '%','N', 'E', 'N', 'E', 'G','!', '?', 'V', "V", "E", "R", "W", "E", "A", "W", "E", "R", "T", "Y", "K", "X", "Z", "A", "",'x','z', 'a', 's', 'u', 'y', 't', 'r', 'e', 'w', 'q', 'f', 'g', 'e', 'd', 'c', 'c', 'b', 'e', 'a', '3', '2', '@', '@', '%', '&', '4', '4', '2', '1']
    dd4= ['D', 'Q', 'B', '#', '$', '2', '@', '^', '1', '%','N', 'E', 'N', 'E', 'G','!', '?', 'V', "V", "E", "R", "W", "E", "A", "W", "E", "R", "T", "Y", "K", "X", "Z", "A", "",'x','z', 'a', 's', 'u', 'y', 't', 'r', 'e', 'w', 'q', 'f', 'g', 'e', 'd', 'c', 'c', 'b', 'e', 'a', '3', '2', '@', '@', '%', '&', '4', '4', '2', '1']
    dd5= ['D', 'Q', 'B', '#', '$', '2', '@', '^', '1', '%','N', 'E', 'N', 'E', 'G','!', '?', 'V', "V", "E", "R", "W", "E", "A", "W", "E", "R", "T", "Y", "K", "X", "Z", "A", "",'x','z', 'a', 's', 'u', 'y', 't', 'r', 'e', 'w', 'q', 'f', 'g', 'e', 'd', 'c', 'c', 'b', 'e', 'a', '3', '2', '@', '@', '%', '&', '4', '4', '2', '1']
    dd6= ['D', 'Q', 'B', '#', '$', '2', '@', '^', '1', '%','N', 'E', 'N', 'E', 'G','!', '?', 'V', "V", "E", "R", "W", "E", "A", "W", "E", "R", "T", "Y", "K", "X", "Z", "A", "",'x','z', 'a', 's', 'u', 'y', 't', 'r', 'e', 'w', 'q', 'f', 'g', 'e', 'd', 'c', 'c', 'b', 'e', 'a', '3', '2', '@', '@', '%', '&', '4', '4', '2', '1']
    dd7= ['D', 'Q', 'B', '#', '$', '2', '@', '^', '1', '%','N', 'E', 'N', 'E', 'G','!', '?', 'V', "V", "E", "R", "W", "E", "A", "W", "E", "R", "T", "Y", "K", "X", "Z", "A", "",'x','z', 'a', 's', 'u', 'y', 't', 'r', 'e', 'w', 'q', 'f', 'g', 'e', 'd', 'c', 'c', 'b', 'e', 'a', '3', '2', '@', '@', '%', '&', '4', '4', '2', '1']
    dd8 = ['D', 'Q', 'B', '#', '$', '2', '@', '^', '1', '%','N', 'E', 'N', 'E', 'G','!', '?', 'V', "V", "E", "R", "W", "E", "A", "W", "E", "R", "T", "Y", "K", "X", "Z", "A", "",'x','z', 'a', 's', 'u', 'y', 't', 'r', 'e', 'w', 'q', 'f', 'g', 'e', 'd', 'c', 'c', 'b', 'e', 'a', '3', '2', '@', '@', '%', '&', '4', '4', '2', '1']
    dd9 = ['D', 'Q', 'B', '#', '$', '2', '@', '^', '1', '%','N', 'E', 'N', 'E', 'G','!', '?', 'V', "V", "E", "R", "W", "E", "A", "W", "E", "R", "T", "Y", "K", "X", "Z", "A", "",'x','z', 'a', 's', 'u', 'y', 't', 'r', 'e', 'w', 'q', 'f', 'g', 'e', 'd', 'c', 'c', 'b', 'e', 'a', '3', '2', '@', '@', '%', '&', '4', '4', '2', '1']
    dd10 = ['D', 'Q', 'B', '#', '$', '2', '@', '^', '1', '%','N', 'E', 'N', 'E', 'G','!', '?', 'V', "V", "E", "R", "W", "E", "A", "W", "E", "R", "T", "Y", "K", "X", "Z", "A", "",'x','z', 'a', 's', 'u', 'y', 't', 'r', 'e', 'w', 'q', 'f', 'g', 'e', 'd', 'c', 'c', 'b', 'e', 'a', '3', '2', '@', '@', '%', '&', '4', '4', '2', '1']
    dd11= ['D', 'Q', 'B', '#', '$', '2', '@', '^', '1', '%','N', 'E', 'N', 'E', 'G','!', '?', 'V', "V", "E", "R", "W", "E", "A", "W", "E", "R", "T", "Y", "K", "X", "Z", "A", "",'x','z', 'a', 's', 'u', 'y', 't', 'r', 'e', 'w', 'q', 'f', 'g', 'e', 'd', 'c', 'c', 'b', 'e', 'a', '3', '2', '@', '@', '%', '&', '4', '4', '2', '1']
    dd12= ['D', 'Q', 'B', '#', '$', '2', '@', '^', '1', '%','N', 'E', 'N', 'E', 'G','!', '?', 'V', "V", "E", "R", "W", "E", "A", "W", "E", "R", "T", "Y", "K", "X", "Z", "A", "",'x','z', 'a', 's', 'u', 'y', 't', 'r', 'e', 'w', 'q', 'f', 'g', 'e', 'd', 'c', 'c', 'b', 'e', 'a', '3', '2', '@', '@', '%', '&', '4', '4', '2', '1']
    dd13= ['D', 'Q', 'B', '#', '$', '2', '@', '^', '1', '%','N', 'E', 'N', 'E', 'G','!', '?', 'V', "V", "E", "R", "W", "E", "A", "W", "E", "R", "T", "Y", "K", "X", "Z", "A", "",'x','z', 'a', 's', 'u', 'y', 't', 'r', 'e', 'w', 'q', 'f', 'g', 'e', 'd', 'c', 'c', 'b', 'e', 'a', '3', '2', '@', '@', '%', '&', '4', '4', '2', '1']
    dd14= ['D', 'Q', 'B', '#', '$', '2', '@', '^', '1', '%','N', 'E', 'N', 'E', 'G','!', '?', 'V', "V", "E", "R", "W", "E", "A", "W", "E", "R", "T", "Y", "K", "X", "Z", "A", "",'x','z', 'a', 's', 'u', 'y', 't', 'r', 'e', 'w', 'q', 'f', 'g', 'e', 'd', 'c', 'c', 'b', 'e', 'a', '3', '2', '@', '@', '%', '&', '4', '4', '2', '1']
    dd15= ['D', 'Q', 'B', '#', '$', '2', '@', '^', '1', '%','N', 'E', 'N', 'E', 'G','!', '?', 'V', "V", "E", "R", "W", "E", "A", "W", "E", "R", "T", "Y", "K", "X", "Z", "A", "",'x','z', 'a', 's', 'u', 'y', 't', 'r', 'e', 'w', 'q', 'f', 'g', 'e', 'd', 'c', 'c', 'b', 'e', 'a', '3', '2', '@', '@', '%', '&', '4', '4', '2', '1']
    dd16= ['D', 'Q', 'B', '#', '$', '2', '@', '^', '1', '%','N', 'E', 'N', 'E', 'G','!', '?', 'V', "V", "E", "R", "W", "E", "A", "W", "E", "R", "T", "Y", "K", "X", "Z", "A", "",'x','z', 'a', 's', 'u', 'y', 't', 'r', 'e', 'w', 'q', 'f', 'g', 'e', 'd', 'c', 'c', 'b', 'e', 'a', '3', '2', '@', '@', '%', '&', '4', '4', '2', '1']


# shuffling the lists for extra random or something.
    random.shuffle(dd1)
    random.shuffle(dd2)
    random.shuffle(dd3)
    random.shuffle(dd4)
    random.shuffle(dd5)
    random.shuffle(dd6)
    random.shuffle(dd7)
    random.shuffle(dd8)
    random.shuffle(dd9)
    random.shuffle(dd10)
    random.shuffle(dd11)
    random.shuffle(dd12)
    random.shuffle(dd13)
    random.shuffle(dd14)
    random.shuffle(dd15)
    random.shuffle(dd16)
# generating password and storing it in a variable, then printing it for the user
    bb=(random.choice(dd1)+random.choice(dd2)+random.choice(dd3)
        +random.choice(dd4)+random.choice(dd5)+random.choice(dd6)+random.choice(dd7)
        +random.choice(dd8)+random.choice(dd9)+random.choice(dd9)+random.choice(dd10)+random.choice(dd11)
        +random.choice(dd12)+random.choice(dd13)+random.choice(dd14)+random.choice(dd15)+random.choice(dd16))
    print(bb)
# saving password to file
    choice = input("Do you want to save the password (Y/N): ")
    account = input("What service are you signing up for: ")

    if choice == "y":
        print("Saving file...")
        with open("password.txt", "a") as p:
            p.write(bb+" - "+account+"\n")
        p.close()

    else:
            print("Your password won't be saved to passwords.txt")
#end of function

# 2 options for user to choose from:
opt = input("Welcome. Please choose from the following options:\n1) Generate password\n2) Print out passwords\n3) Save external passworf\n:: ")
if ((opt.lower() == "1") or (opt.lower() == "generate password") or (opt.lower() == "generate")):
    print("Your password will be generated shortly...")
    passgen()

if ((opt == "2") or (opt.lower() == "print") or (opt.lower() == "print out") or
        (opt.lower() == "passwords") or (opt.lower() == "print out passwords")):
    print("Printing out passwords...")
    pass_out()

if ((opt == "3") or (opt.lower() == "save") or (opt.lower() == "save external password")):
    print("Loading function...")
    pass_in()