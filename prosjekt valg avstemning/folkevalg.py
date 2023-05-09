from typing import OrderedDict


users = {}
status = ""

candidates_1= "Isak"
candidates_2= "Magnus"

candidate_1_votes= 0
candidate_2_votes= 0

candidates = OrderedDict()
candidates = {
    "Isak" : 0,
    "Magnus" : 0
}

def displayMenu():
    candidate_number = input("Are you registered user? y/n? Press q to quit")

def electionmenu():
    all_candidates_string = ""
    
    for index, candidate in enumerate(candidates.keys()):
        all_candidates_string += "\n" + str(index) + ") " + candidate


    vote = input("Vote for candidates: " + all_candidates_string)
    print(vote)
        

def newUser():
    createLogin = input("input youre school email: ")
 
    if createLogin in users:
        print("\n account already exist using the current email!\n")
    else:
        createPassw = input("Create password: ")
        users[createLogin] = createPassw
        print("\n Account created\n")
    print("new user finished")
 
def oldUser():
    login = input("Enter email: ")
    passw = input("Enter password: ")
 
    if login in users and users[login] == passw:
        print("\nLogin successful!\n")
    else:
        print("\nUser doesn't exist or wrong password!\n")
    print("old user finished")
    print ("Welcome to Teh yearly IM election")
    print 

 
while status != "q":
    displayMenu();
    newUser()

def opening():
    print("IM Election booth\n\n ")
    print("Login")
    print("Create account")

def opening_login():
    print("Email:")
    print("Password:")

def opening_create():
    print("fill in youre school email and create password")
    print("Email:")
    print("Password:")

def opening_succsesful():
    print("Login succsesful :)")

def opening_candidate():
    print("Candidate 1 Isak\n")
    print("Candidate 2 Magnus")
    print("To vote input ID number of candidate")

def opening_close():
    print("Thanks for youre vote :)")
    
def runCode():
    # This function if responsible for the running of the app!
    pass

