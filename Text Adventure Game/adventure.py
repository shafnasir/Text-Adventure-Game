from game_data import World, Item, Location
from player import Player

if __name__ == "__main__":
    WORLD = World("map.txt", "locations.txt", "items.txt")
    PLAYER = Player(0,0) # set starting location of player; you may change the x, y coordinates here as appropriate

    menu = ["look", "inventory", "score", "quit", "back"]
    print("\nYou have overslept and have woken up in the UTM library and you notice you are missing some items you need for your exam.\n"
          "Your task is to find your T card, test cheat sheet, lucky pen and maybe buy some coffee if you have time and get to your\nexam on time\n")

    # All the variables used in adventure.py
    past_locations = []
    used_items = []
    choice = ''
    score = 0
    moves = 0

    while not PLAYER.victory:
        location = WORLD.get_location(PLAYER.x, PLAYER.y)
        item = WORLD.get_item(PLAYER.x, PLAYER.y)

        print("What to do? \n")
        print("[menu]")

        if choice == "look":
            print(location.get_full_description())

        elif location.get_index() in past_locations: # if the player has already been in that location print the brief
            print(location.get_brief_description())
        else:
            print(location.get_full_description()) # else print full description and add it to past_locations
            past_locations.append(location.get_index())
            score = score + int(location.get_points())

        choice = input("\nEnter action: ")

        if (choice == "[menu]"): # prints all the available actions in that location
            print("Menu Options: \n")
            for option in location.available_actions():
                print(option)
            choice = input("\nChoose action: ")

        # Code for the direction the user chooses
        if choice == "GO west":
            # if at that location its a valid move
            if choice in location.available_directions():
                PLAYER.move_west()
                moves += 1

            else:
                print("That way is blocked")

        if choice == "GO east":

            if choice in location.available_directions():
                PLAYER.move_east()
                moves += 1

            else:
                print("That way is blocked")

        if choice == "GO north":
             if choice in location.available_directions():
                 PLAYER.move_north()
                 moves += 1

             else:
                print("That way is blocked")

        if choice == "GO south":
            if choice in location.available_directions():
                PLAYER.move_south()
                moves += 1

            else:
                print("That way is blocked")

        if choice == "get item":
            #if their at a location with an item and they havent already been got the item
            for g in [(1,0),(2,0),(1,3),(1,1)]:
                if g == (PLAYER.x, PLAYER.y):
                    if item.get_name() in PLAYER.get_inventory():
                            print("you already got that item")
                    else:
                        PLAYER.add_item(item.get_name())
                        score = score + 1

        if choice == "use item":
            #if they have the right item and their at the right location then
            if location.get_index() == "3":
                if 'money ' in PLAYER.get_inventory():
                    used_items.append(item.get_name())
                    PLAYER.remove_item("money ")
                    score = score + 1
                    print("You have bought coffee from StarBucks!")
            if location.get_index() == "8":
                while True:
                    for i in PLAYER.get_inventory():
                        if i in ['lucky pen ','t card ','test cheat sheet ']:
                            used_items.append(i)
                            PLAYER.remove_item(i)
                        else:
                            print("you don't have any items to use")
                    if PLAYER.get_inventory() == []:
                        break


        if choice == "inventory":
            print("Inventory:",PLAYER.get_inventory()) # prints the players inventory

        if choice == "quit": #Exit the program when they quit
            exit()

        if choice == "score":
            print(score)

        if moves > 15: # if the player moves more than 15 times they automatically lose
            print("Sorry you used to many moves, moves: {0}".format(moves))
            exit()

        if location.get_index() == "8": # IF they are in the last location, have under 15 moves and all three items are used then the player wins
            if moves <= 15:
                if 'lucky pen ' in used_items and 't card ' in used_items and 'test cheat sheet ' in used_items:
                    print("Congratulations you won the game! in {0} moves and your score is {1}".format(moves,score))
                    PLAYER.victory = True
