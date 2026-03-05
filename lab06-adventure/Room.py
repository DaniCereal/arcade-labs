class Room:
    """
    This is a class that represents one of the multiple rooms
    """
    def __init__(self):
        """ This is a method that sets up the variables in the object. """
        self.description = ""
        self.north = 0
        self.west = 0
        self.east = 0
        self.south = 0
    
    def __init__(self, description, north, east, west, south):
        self.description = description
        self.north = north
        self.west = west
        self.east = east
        self.south = south

def main():
    RoomList = []

    # This creates all the rooms. The constructor expects a description, then the North, East, West and South
    room3 = Room("You appear in an unknown location.\n" \
    "you can smell the trays of blood and despair\n" \
    "You can hear a big roar from the north\n" \
    "You are presented with 3 doors, one to the north, one to the east and the last one to the south\n", 1, 4, 2, 6)
    room4 = Room("Crossing through the left door, you come across some epstein flies, seeing they can't do anything to you, they fly across the room and leave through the door you have just left\n" \
    "Seems like a dead end\n", None, None, 3, None)
    room2 = Room("Although it just looked like a wall, you take a closer look to the wall, it seems normal at first but then a weird smell comes from the inside\n" \
    "you decide to hit the wall, not really knowing what to expect and then...\n" \
    "A new room appears right before you. You can see a big coin floating\n", 0, 3, None, 5)
    room0 = Room("Congratulations! The big golden gates are upon you, enjoy your reward...\n" \
    "wait...\n" \
    "is that a key? Maybe it'll be useful somewhere...\n", None, 1, None, 2)
    room5 = Room("Stepping into the room, the floor is littered with cracked stones and old stains\n" \
    "A pair of sleepy chargers snort at you from the corner, then lazily wander in circles as if they forgot why they woke up\n" \
    "One of the walls has a small hole that whistles quietly with dungeon wind\n" \
    "Nothing much here — just another empty room\n", 2, 6, None, None)
    room6 = Room("Passing through the narrow doorway, the room opens into a crooked hallway lined with dusty shelves\n" \
    "A flickering lantern hangs above a wooden door marked with a faded coin symbol\n" \
    "The shop door creaks slightly, as if someone inside is shifting piles of trinkets and junk\n" \
    "You can almost hear the faint jingle of coins from the other side\n", 3, None, 5, 7)
    room7 = Room("The greedy figures welcomes you, sitting in the middle of the room\n" \
    "You can see some slots machine, lit by the only light source, a small fire next to it\n" \
    "The trader smirks and shows a long sword, ready to be used by someone\n" \
    "You don't really understand his words but you know he wants money \n", 6, None, None, None)
    room1 = Room("Walking through the cracked doorway, the air suddenly feels heavier\n" \
    "Torches burn a little brighter here, casting long shadows across the stone floor\n" \
    "At the far end of the room stands a massive door reinforced with dark metal bands\n" \
    "A crude skull symbol is carved into its surface, staring back at you\n" \
    "This must be the boss door — whatever is behind it is waiting\n", 8, None, 0, 3)
    room8 = Room("You push open the heavy door and step into a wide, circular chamber\n" \
    "The walls are scarred with deep cracks, and the ground is smeared with old, dark stains\n" \
    "A low growl echoes through the room as something stirs in the shadows\n" \
    "Suddenly, a massive creature lurches forward from the center of the arena\n" \
    "The boss fight has begun\n", None, None, None, None)
    #We add all the rooms to the room list
    RoomList.append(room0)
    RoomList.append(room1)
    RoomList.append(room2)
    RoomList.append(room3)
    RoomList.append(room4)
    RoomList.append(room5)
    RoomList.append(room6)
    RoomList.append(room7)
    RoomList.append(room8)
    currentRoom = 3
    
    done = False
    #Until we are done, we will keep going through rooms
    while(done == False):
        #We print an empty space to make it more visual and then the description of the current room
        print()
        print(RoomList[currentRoom].description)
        newDirection = input("Where you do want to go? (North, West, East, South)")
        if(newDirection.upper() == "N" or newDirection.upper() == "NORTH"):
            nextRoom = RoomList[currentRoom].north
            if (nextRoom == None):
                print("You can’t go that way")
            else: 
                currentRoom = nextRoom
        elif(newDirection.upper() == "S" or newDirection.upper() == "SOUTH"):
            nextRoom = RoomList[currentRoom].south
            if (nextRoom == None):
                print("You can’t go that way")
            else: 
                currentRoom = nextRoom
        elif(newDirection.upper() == "W" or newDirection.upper() == "WEST"):
            nextRoom = RoomList[currentRoom].west
            if (nextRoom == None):
                print("You can’t go that way")
            else: 
                currentRoom = nextRoom
        elif(newDirection.upper() == "E" or newDirection.upper() == "EAST"):
            nextRoom = RoomList[currentRoom].east
            if (nextRoom == None):
                print("You can’t go that way")

            else: 
                currentRoom = nextRoom
        elif(newDirection.upper() == "EXIT"):
            done = True
        else:
            print("I don't think that's a direction")

        if(currentRoom == 8):
            print()
            print(RoomList[currentRoom].description)
            done = True
        
main()