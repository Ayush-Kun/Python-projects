def login():
    pass

def signup():
    user = input("what is the username: ")
    pwd = input("What is the password: ")

    with open('signup.txt', 'a') as f:
        f.write(user + '|' + pwd + "\n")


while True:
    in_put = input("What do you want to do, Login or signup? (login, signup): ")

    if (in_put == 'q'):
        break

    if (in_put == 'login'):
        login()
       

    if (in_put == 'signup' ):
        signup()

