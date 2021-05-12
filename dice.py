import random
def generating_dice(choice):
    if choice.lower() == "go":
        return random.randint(1, 6)
    return 0

