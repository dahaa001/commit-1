users = {}
status = ""
 
def displayMenu():
    status = input("(Are you registered user? yes/no? Press q to quit)")
    if status == "yes":
        oldUser()
    elif status == "no":
        newUser()
 
def newUser():
    createLogin = input("Create login name: ")
 
    if createLogin in users:
        print("\nLogin name already exist!\n")
    else:
        createPassw = input("Create password: ")
        users[createLogin] = createPassw
        print("\nUser created\n")
 
def oldUser():
    login = input("Enter login name: ")
    passw = input("Enter password: ")
 
    if login in users and users[login] == passw:
        print("\n Welcom to the woting booth!\n")
    else:
        print("\nUser doesn't exist or wrong password!\n")
 
while status != "q":
    displayMenu()   

def timevote():
    status = input("(Do you want to vote?)")
    if status == "yes":
        candidates()
    elif status == "no":
        newUser()

def candidates():
    

