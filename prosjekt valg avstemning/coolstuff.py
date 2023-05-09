users = {"magnustvilde": "pass123"}
status = ""


def opening_login():
    print("IM Election booth\n\n ")
    print("Login")
    print("Create account")

def opening_login():
    emailCheck = input("Email:")
    passwordCheck = input("Password:")

def opening_create():
    print("fill in youre school email and create password")
    email = input("Email:")
    password = input("Password:")
    return email, password

def opening_succsesful():
    print("Login succsesful :)")

def opening_candidate():
    print("Candidate 1 Isak\n")
    print("Candidate 2 Magnus")
    print("To vote input ID number of candidate")

def opening_close():
    print("Thanks for youre vote :)")

def runCode():
     status = input("(Welcome to IM Election booth\n\n Are you registered voter? yes/no? )")
     if status == "yes":
        opening_login()
     elif status == "no":
        email, password = opening_create()
    
        # This function if responsible for the running of the app!
    
runCode()