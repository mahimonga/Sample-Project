#check_win 
import sys
MAX_VAL = 100
def check_win(player_name, position):
    if MAX_VAL == position:
        print("\nCongratulations!!")
        print("\nYou won the game!!")
        print("\nDo you want to play again? If yes press p.\nIf no, to quit, press q.")
        press = input()
        if press == "q":
            sys.exit(1)
        else:
            welcome_msg()

