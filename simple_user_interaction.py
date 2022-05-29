game_list = [1,2,3]

def display_game():
    print("Here is the current list")
    print(game_list)

def position_choice():
    
    choice = 'wrong'
    
    while choice not in ['0','1','2']:
        choice = input("Enter a position : 0 , 1 or 2: ")
        
        if choice not in ['0','1','2']:
            print("Invalid input")
        else: pass
    return int(choice)

def replacement_choice(gamelist,position):
    replacement = input(f"Type the string to place at {position} position: ")
    gamelist[position] = replacement 
    return gamelist

def gameon_choice():
    
    choice = 'wrong'
    
    while choice not in ['Y','N']:
        choice = input('Would you like to keep playing ? Y or N ')
        
        if choice not in ["Y","N"]:
            print("Invalid input! Please choose Y or N")
    if choice == 'Y':
        return True
    else:
        return False

gameon = True 
while gameon:
    display_game()
    position = position_choice()
    gamelist = replacement_choice(game_list,position)
    gameon = gameon_choice()