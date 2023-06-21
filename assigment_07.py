
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
a = input("You are at a crooosroad, where do you want to go ? Type Left or right?\n")
f = input("You are at a crooosroad, where do you want to go ? Type Left or right?\n").lower()
print(f)

if a == "left" or a == "Left" or a == "LEFT":
    b = input('You are come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to Swim  across \n')
    if b == "wait" or b == "Wait" or b == "WAIT":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yeelow  and one blue. Which colour do you choose?\n")
        if door == "Blue" or door == "blue" or door == "BLUE":
            print("Eaten by beasts.")
            print("Game Over.")
        elif door == "Red" or door == "red" or door == "RED":
            print("Burned by fire.")
            print("Game Over.")
        elif door == "Yellow" or door == "yellow" or door == "YELLOW":
            print("You Win!")
        else:
            print("You chose a door that doesn't exist.")
            print("Game Over.")
    else:
        print("Attacked b trout.")
        print("Game Over.")

else:
    print("Fall into a hole.")
    print("Game Over")

            
