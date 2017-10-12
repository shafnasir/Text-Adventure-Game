class Location:

    def __init__(self, index, points, brief, long, actions, directions):
        '''Creates a new location.

        Data that could be associated with each Location object:
        a position in the world map,
        a brief description,
        a long description,
        a list of available commands/directions to move,
        items that are available in the location,
        and whether or not the location has been visited before.
        Store these as you see fit.

        This is just a suggested starter class for Location.
        You may change/add parameters and the data available for each Location class as you see fit.
  
        The only thing you must NOT change is the name of this class: Location.
        All locations in your game MUST be represented as an instance of this class.
        '''
        self.index = index
        self.points = points
        self.brief = brief
        self.long = long
        self.actions = actions
        self.directions = directions

    def get_brief_description (self):
        '''Return str brief description of location.
        '''
        return self.brief

    def get_full_description(self):
        '''Return str long description of location.
        >>> WORLD = World("map.txt", "locations.txt", "items.txt")
        >>> WORLD.locations[0].get_full_description()
        'that way is blocked. '
        '''
        return self.long

    def available_actions(self):
        '''
        -- Suggested Method (You may remove/modify/rename this as you like) --
        Return list of the available actions in this location.
        The list of actions should depend on the items available in the location
        and the x,y position of this location on the world map.
        '''
        return self.actions

    def get_index(self):
        '''
        :return: This function returns the index of the current location
        '''
        return self.index

    def available_directions(self):
        '''
        This method is to return all the possible directions in the current location
        '''
        return self.directions

    def get_points(self):
        '''
        :return: number of points each location has
        '''
        return self.points

class Item:

    def __init__ (self, name, start, target, target_points):
        '''Create item referred to by string name, with integer "start"
        being the integer identifying the item's starting location,
        the integer "target" being the item's target location, and
        integer target_points being the number of points player gets
        if item is deposited in target location.

        This is just a suggested starter class for Item.
        You may change these parameters and the data available for each Item class as you see fit.
        Consider every method in this Item class as a "suggested method":
                -- Suggested Method (You may remove/modify/rename these as you like) --

        The only thing you must NOT change is the name of this class: Item.
        All item objects in your game MUST be represented as an instance of this class.
        '''
        self.name = name
        self.start = start
        self.target = target
        self.target_points = target_points

    def get_starting_location (self):
        '''Return int location where item is first found.'''
        return self.start

    def get_name(self):
        '''Return the str name of the item.'''
        return self.name

    def get_target_location (self):
        '''Return item's int target location where it should be deposited.'''
        return self.target

    def get_target_points (self):
        '''Return int points awarded for depositing the item in its target location.'''
        return self.target_points


class World:

    def __init__(self, mapdata, locdata, itemdata):
        '''
        Creates a new World object, with a map, and data about every location and item in this game world.

        You may ADD parameters/attributes/methods to this class as you see fit.
        BUT DO NOT RENAME OR REMOVE ANY EXISTING METHODS/ATTRIBUTES.

        :param mapdata: name of text file containing map data in grid format (integers represent each location, separated by space)
                        map text file MUST be in this format.
                        E.g.
                        1 -1 3
                        4 5 6
                        Where each number represents a different location, and -1 represents an invalid, inaccessible space.
        :param locdata: name of text file containing location data (format left up to you)
        :param itemdata: name of text file containing item data (format left up to you)
        :return:
        '''
        self.map = self.load_map(mapdata) # The map MUST be stored in a nested list as described in the docstring for load_map() below
        self.locations = [] #... You may choose how to store location and item data.
        self.items = []
        self.load_locations(locdata) # This data must be stored somewhere. Up to you how you choose to do it...
        self.load_items(itemdata) # This data must be stored somewhere. Up to you how you choose to do it...

    def load_map(self, filename):
        '''
        THIS FUNCTION MUST NOT BE RENAMED OR REMOVED.
        Store map from filename (map.txt) in the variable "self.map" as a nested list of integers like so:
            1 2 5
            3 -1 4
        becomes [[1,2,5], [3,-1,4]]
        RETURN THIS NEW NESTED LIST.
        :param filename: string that gives name of text file in which map data is located
        :return: return nested list of integers representing map of game world as specified above"

        '''
        self.MAP = []
        file = open(filename, "r")
        for line in file:
            self.MAP.append(line.strip().split())
        file.close()
        return self.MAP

    def load_locations(self, filename):
        '''
        Store all locations from filename (locations.txt) into the variable "self.locations"
        however you think is best.
        Remember to keep track of the integer number representing each location.
        Make sure the Location class is used to represent each location.
        Change this docstring as needed.
        :param filename:
        :return:
        '''
        file = open(filename, "r")
        r = file.readlines()
        points = 0
        brief = ""
        long = ""
        directions = " "
        actions = ''

        for i in range(len(r)):
            b= ''
            l = ''
            d = ""
            try:
                r[i]= r[i].strip().split()

                if r[i][0] == "LOCATION":
                    index = r[i][1]

                elif r[i][0].isdigit():
                    points = r[i][0]

                elif r[i][0] == "brief":
                    del r[i][0]
                    for j in range(len(r[i])):
                        b = b + r[i][j] + " "
                    brief = b

                elif r[i][0] == "long":
                    del r[i][0]
                    for j in range(len(r[i])):
                        l = l + r[i][j] + " "
                    long = l

                elif r[i][0] == "actions":
                    del r[i][0]
                    actions = r[i]
                    for j in range(len(actions)):
                        actions[j] = actions[j].replace(","," ")

                elif r[i][0] == "directions":
                    del r[i][0]
                    directions = r[i]
                    for j in range(len(directions)):
                        directions[j] = directions[j].replace(","," ")

                    loc = Location(index, points, brief, long, actions, directions)
                    self.locations.append(loc)

            except IndexError:
                pass

    def load_items(self, filename):
        '''
        Store all items from filename (items.txt) into ... whatever you think is best.
        Make sure the Item class is used to represent each item.
        Change this docstring accordingly.
        :param filename:
        :return:
        '''
        file = open("items.txt", "r")
        x = file.readlines()
        start = 0
        target = 0
        target_points = 0

        for i in range(len(x)):
            x[i]=x[i].strip().split()
            name = ''

            for j in range(3,len(x[i]),1):
                name = name + x[i][j] + ' '
            start = x[i][0]
            target = x[i][1]
            target_points = x[i][2]

            itm = Item(name, start, target, target_points)
            self.items.append(itm)

    def get_location(self, x, y):
        '''Check if location exists at location (x,y) in world map.
        Return Location object associated with this location if it does. Else, return None.
        Remember, locations represented by the number -1 on the map should return None.
        :param x: integer x representing x-coordinate of world map
        :param y: integer y representing y-coordinate of world map
        :return: Return Location object associated with this location if it does. Else, return None.

        '''
        world_map = World("map.txt","locations.txt","items.txt").load_map("map.txt")
        if world_map[y][x] == "-1":
            return None
        else:
            return (self.locations[int(world_map[y][x])]) #supposed to return the object for the location

    def get_item(self, x, y):
        '''
        Check if item exists at location (x,y) in world map.
        Return item object associated with this location if it does. Else, return None.
        :param x: integer x representing x-coordinate of world map
        :param y: integer y representing y-coordinate of world map
        :return: Return item object associated with this location if it does. Else, return None.
        '''
        if (x,y)== (1,0):
            return self.items[0]
        if (x,y)==(2,0):
            return self.items[1]
        if (x,y)==(1,3):
            return self.items[2]
        if (x,y)==(1,1):
            return self.items[3]
        else:
            return None

