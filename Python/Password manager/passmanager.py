master_pwd = input("What is the master password?")

def view():
     with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = (line.rstrip())
            user, passw = data.split("|")
            print("User:", user, "Password:", passw)
    
def add():
    name = input('Account name: ')
    password = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + password + "\n")

while True:
    mode = input("What do you want to do,view the password or add one?(add, view) or press q for exit: ")

    if (mode=='q'):
        break

    if (mode=='add'):
        add()
    elif (mode=='view'):
        view()
    else:
        print("Invalid mode.")
        continue

