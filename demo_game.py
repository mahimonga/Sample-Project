import pygame
import random
import time

pygame.init()

width = 1366
height = 786

window = pygame.display.set_mode((width, height))
icon = pygame.image.load("Snakes-N-Ladders\icon.jpg")
pygame.display.set_caption("Snakes and ladders")
pygame.display.set_icon(icon)
pygame.display.update()

#colors
black = (0, 0, 0)
purple = (153, 0, 153)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

board = pygame.image.load("Snakes-N-Ladders\Board.jpg")
dice1 = pygame.image.load("Snakes-N-Ladders\dice1.png")
dice2 = pygame.image.load("Snakes-N-Ladders\dice2.png")
dice3 = pygame.image.load("Snakes-N-Ladders\dice3.png")
dice4 = pygame.image.load("Snakes-N-Ladders\dice4.png")
dice5 = pygame.image.load("Snakes-N-Ladders\dice5.png")
dice6 = pygame.image.load("Snakes-N-Ladders\dice6.png")
red_coin = pygame.image.load("Snakes-N-Ladders\redcoin.png")
blue_coin = pygame.image.load("Snakes-N-Ladders\bluecoin.png")

#function for mouse position
mouse = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()

#function for message on buttons
def message_display(text,x,y,fs):
    largeText = pygame.font.Font('freesansbold.ttf',fs)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x,y)
    GD.blit(TextSurf, TextRect)

def text_objects(text, font):
    textSurface = font.render(text, True,white)
    return textSurface, textSurface.get_rect()

#function for coin movement
def goti(a):
    l1=[[406,606],[456,606],[506,606],[556,606],[606,606],[656,606],[706,606],[756,606],[806,606],[856,606],[906,606],[906,560],[856,560],[806,560],[756,560],[706,560],[656,560],[606,560],[556,560],[506,560],[456,560],[456,506],[506,506],[556,506],[606,506],[656,506],[706,506],[756,506],[806,506],[856,506],[906,506],[906,460],[856,460],[806,460],[756,460],[706,460],[656,460],[606,460],[556,460],[506,460],[456,460],[456,406],[506,406],[556,406],[606,406],[656,406],[706,406],[756,406],[806,406],[856,406],[906,406],[906,360],[856,360],[806,360],[756,360],[706,360],[656,360],[606,360],[556,360],[506,360],[456,360],[456,306],[506,306],[556,306],[606,306],[656,306],[706,306],[756,306],[806,306],[856,306],[906,306],[906,260],[856,260],[806,260],[756,260],[706,260],[656,260],[606,260],[556,260],[506,260],[456,260],[456,206],[506,206],[556,206],[606,206],[656,206],[706,206],[756,206],[806,206],[856,206],[906,206],[906,160],[856,160],[806,160],[756,160],[706,160],[656,160],[606,160],[556,160],[506,160],[456,160]]
    l2=l1[a]
    x=l2[0]-25
    y=l2[1]-25
    return x,y

#function for ladders
step = {1:38, 4:14, 9:31, 21:42, 28:84, 51:67, 72:91, 80:99}
def ladders(x):
    if x in step.keys():
        final_val = step[x]
        return final_val
    return x

#function for snakes
snake = {17:7, 54:34, 62:19, 64:60, 87:36, 92:73, 95:75, 98:79}
def snakes(x):
    if x in snake.keys():
        final_val = snake[x]
        return final_val
    return x

#function for dice
def generating_dice_number(choice):
    if choice.lower() == "go":
        return random.randint(1, 6)
    return 0

#function for displaying dice images
value_to_image = {1:dice1, 2:dice2, 3:dice3, 4:dice4, 5:dice5, 6:dice6}
def dice(x):
    a = generating_dice_number(x)
    if a in value_to_image.keys():
        image = value_to_image[a]
        
    time=pygame.time.get_ticks()
    while pygame.time.get_ticks()-time<1000:
        window.blit(a,(300,500))
        pygame.display.update()

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
        print("\nIt's player 1's turn! Enter Go to roll the dice.")
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




