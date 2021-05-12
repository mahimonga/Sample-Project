from dice import *
from check_win import *
from snake_ladder import *
from players import *

def invalid():
     print("Invalid option chosen. Please try again.")
def welcome_msg():
    print("Welcome to snakes and Ladders! Let's play!")


def play():
    welcome_msg()
    player1_name = players()
    player2_name = players()   
    player1_current, player2_current = 0, 0

    while True:
        print("\nIt's player " + player1_name +"'s turn! Enter Go to roll the dice.")
        option = input()
        dice_val = generating_dice(option)
        while dice_val == 0:
            invalid()
            option = input()
            dice_val = generating_dice(option)
        print("You rolled a " + str(dice_val) + "!")
        player1_current = snake_ladder(player1_name, player1_current, dice_val)

        check_win(player1_name, player1_current)
        
        print("\nIt's player 2's turn! Enter Go to roll the dice.")
        option2 = input()
        dice_val2 = generating_dice(option2)
        while dice_val2 == 0:
            invalid()
            option2 = input()
            dice_val2 = generating_dice(option2)
        print("You rolled a " + str(dice_val2) + "!")
        player2_current = snake_ladder(player2_name, player2_current, dice_val2)
        
        check_win(player2_name, player2_current)

if __name__ == "__main__":
    play()



