from asyncore import write
import random
x_wins = 0
o_wins = 0
user = True


def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print()

def quit(user_input):
    if user_input.lower() == "q": 
        print("Thanks for playing")
        return True
    else: return False

def check_input(user_input):
    # check if its a number
    if not isnum(user_input): return False
    user_input = int(user_input)
    # check if its 1 - 9
    if not bounds(user_input): return False
    return True

def isnum(user_input):
    if not user_input.isnumeric(): 
        print("This is not a valid number pleas try again")
        return False
    else: return True

def bounds(user_input):
    if user_input > 9 or user_input < 1: 
        print("This is number is out of bounds")
        return False
    else: return True

def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":
        print("This position is already taken pay atention!")
        return True
    else: return False

def istaken_computer(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":
        return True
    else: return False

def coordinates(user_input):
    row = int(user_input / 3)
    col = user_input
    if col > 2: col = int(col % 3)
    return (row,col)

def add_to_board(coords, board, active_user):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user

def current_user(user):
    if user: return "x"
    else: return "o"

def iswin(user, board):
    if check_row(user, board): return True
    if check_col(user, board): return True
    if check_diag(user, board): return True
    return False

def isFull(board):
    for row in board:
        for cell in row:
            if cell == "-":
                return False
    return True

def check_row(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        if complete_row: return True
    return False 

def check_col(user, board):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != user:
                complete_col = False
                break
        if complete_col: return True
    return False

def check_diag(user, board):
  #top left to bottom right
  if board[0][0] == user and board[1][1] == user and board[2][2] == user: return True
  elif board[0][2] == user and board[1][1] == user and board[2][0] == user: return True
  else: return False

def menu():
    print ("Menu")
    print("[1] Local 1v1")
    print("[2] Play with Ai")
    print("[3] Grafic settings")
    print("[4] Exit program ")
    
def play_ai_menu():
    print ("Menu")
    print("[1] Play with Ai")
    print("[2] Go back")

    
def menu_ai():
    print ("Menu")
    print("[1] Smarte Ai")
    print("[2] Dumb Ai")
    print("[3] Go back")

def play_error():
    print("error")
    print("404")

def clear():
    print("\n" * 50)
    exit(0)
    clear()

def smart_ai(board, character):
    best_score = -800
    best_coords = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] != "-":
                continue
            board[i][j] = character
            score = minimax(board, 0, False, character)
            board[i][j] = "-"
            if score > best_score:
                best_score = score
                best_coords = (i, j)
    return best_coords
    


def minimax(board, depth, isMaximizing, character):
    if (iswin(character, board)):
        return 1
    elif (iswin("o" if character == "x" else "x", board)):
        return -1
    elif (isFull(board)):
        return 0

    if (isMaximizing):
        bestScore = -800
        for key in range(9):
            x_coord, y_coord = coordinates(key)
            if (board[x_coord][y_coord] == '-'):
                board[x_coord][y_coord] = character
                score = minimax(board, depth + 1, False, character)
                board[x_coord][y_coord] = '-'
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        for key in range(9):
            x_coord, y_coord = coordinates(key)
            if (board[x_coord][y_coord] == '-'):
                board[x_coord][y_coord] = "o" if character == "x" else "x"
                score = minimax(board, depth + 1, True, character)
                board[x_coord][y_coord] = '-'
                if (score < bestScore):
                    bestScore = score
        return bestScore


def start_game_ai(difficulty, playerChoice):
    x_wins = 0
    o_wins = 0    
    
    print("game startet with difficulty", difficulty, ". You have chosen to be ", playerChoice)
    if(playerChoice == "x"):
        computer = "o"
    else:
        computer = "x"
    while True:
        Draw_nobodywon = 0

        board = [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
        ]
        yourturn = True
        turns = 0
        while turns < 9:
            if yourturn:
                ## Bruker velger og skrives til brett
                print_board(board)
                user_input = input("Please enter a position 1 through 9 or enter \"q\" to quit:")
                if quit(user_input):
                    print("Computer won in total", x_wins, "times.")
                    print("you won", o_wins, "times.")
                    print("Total moves done this game:", Draw_nobodywon)
                    print("Goodbye!")
                    return
                if not check_input(user_input):
                    print("Please try again.")
                    continue
                user_input = int(user_input) - 1
                coords = coordinates(user_input)
                if istaken(coords, board):
                    print("Please try again.")
                    continue
                add_to_board(coords, board, playerChoice)
                if iswin(playerChoice, board): 
                    print_board(board)
                    print(f"Congratulation you won as{playerChoice.upper()}!")
                    x_wins += 1
                    break
            else:
                ## datamaskin velger og skrives til brett
                if difficulty == 2:
                    random_number = random.randint(1, 9)-1
                    coords = coordinates(random_number)
                    while istaken_computer(coords, board):
                        random_number = random.randint(1, 9)-1
                        coords = coordinates(random_number)
                    add_to_board(coords, board, computer)
                    print_board(board)
                    print ("\n")
                else:
                    x, y = smart_ai(board, computer)
                    board[x][y] = computer

            if iswin(computer, board): 
                    print_board(board)
                    print(f"Congratulation you lost to dumb ai,computer won as {computer.upper()}!")
                    x_wins += 1
                    break    
                
            turns += 1
            if turns == 9: print("Tie try again!")
            if yourturn == True:
                yourturn = False
            else: 
                yourturn = True  
            Draw_nobodywon += 1        
        
        print("Computer won in total", x_wins, "times.")
        print("you won", o_wins, "times.")
        print("Total moves done this game:", Draw_nobodywon + 1)
        print("Goodbye!")

        

    



def main_menu():


    while True:
        menu()
        option = int(input("Enter you option "))
        while option != 0:
            if option == 1:
                # do option 1 stuff
                print("option 1 has been called.")
                character = ""
                while character != "x" and character != "o":
                    character = input("choose game character, x or o\n")
                global user
                user = character == "x"
                return
    
            elif option == 2:
                #do option 2 stuff
                print("option 2 has been called.")
                play_ai_menu()
                option = int(input("Enter you option "))
                if option == 1:
                    menu_ai()
                    aioption = int(input("Select degree of difficulty"))
                    playerChoice = input("choose game character, x or o\n")
                    
                    start_game_ai(aioption, playerChoice)
                if option == 1:
                    smart_ai

                if option == 2:
                    next


            elif option == 3:
                #do option 3 stuff
                print("option 3 has been called.\n")
                play_error()

            elif option == 4:
                #do option 4 stuff
                print("option 4 has been called.")
                clear()
            else:
                print("Invalid action")
            print()
            menu()
            option = int(input("Enter you option: "))
        print("Thanks for using this software/game. ")
                
        break
  
main_menu()



while True:
    Draw_nobodywon = 0 
    board = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]
    ]
    yourturn = True
    if yourturn == True:
        yourturn = False
    else: 
        yourturn = True
    

    turns = 0
    while turns < 9:
        active_user = current_user(user)
        print_board(board)
        user_input = input("Please enter a position 1 through 9 or enter \"q\" to quit:")
        if quit(user_input): break
        if not check_input(user_input):
            print("Please try again.")
            continue
        user_input = int(user_input) - 1
        coords = coordinates(user_input)
        if istaken(coords, board):
            print("Please try again.")
            continue
        add_to_board(coords, board, active_user)
        if iswin(active_user, board): 
            print_board(board)
            print(f"Congratulation {active_user.upper()} won!")
            x_wins += 1
            break
    
        
        turns += 1
        if turns == 9: print("Tie try again!")
        user = not user
        Draw_nobodywon += 1
    
    print("You won total", x_wins, "times.")
    print("Opponent won", o_wins, "times.")
    print("Total moves done:", Draw_nobodywon + 1)
    print("Goodbye!")
