from art import logo
print(logo)

something =True
while something == True:
    print("Welcome to Treasure Island \nYour mission is to find the treasure.")
    print("Lets start ")
    print("Ooo the road ends, you have two choices to go left or right")
    
    direction = input("Where do you want to go left or right ")
    direct = direction.lower()
    if direct == "left":
        print("There is a huge river in front of you")
        water = input("do you want to swin or wait.")
        wat = water.lower()
        if wat == "wait":
            print("Three doors appears in front of you: ")
            hel = input("In what colour door you want to go red , yellow or blue.")
            door = hel.lower()
            if door == "red":
                print("You died in fire")
                print("Game Over")
            if door == "blue":
                print("You died in lava")
                print("Game Over")
            if door == "yellow":
                print("You found the tresure")
                print("YOU WIN !")
        else:
            print("Sorry you drowned")
            print("Game Over")
    else:
        print("There was a tiger waiting for you ")
        print("Game Over")
    ending = input("Do you want to play this game again press 'y' for yes and press 'n' for no :")
    end = ending.lower()
    if end=='n':
        something = False