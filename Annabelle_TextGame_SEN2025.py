
import time
import sys

# import time
# import sys

# def typing_effect(text, delay=10):
#     """Prints text to the console with a typing effect.

#     Args:
#         text (str): The text to be printed.
#         delay (float, optional): Delay between characters in seconds. Defaults to 0.05.
#     """
#     for char in text:
#         sys.stdout.write(char)
#         sys.stdout.flush()
#         time.sleep(delay)

# # Example usage:
# typing_effect("Hello, this is a typing effect!", delay=0.1)

print('
      _______________________________________________________________________ 
     (                                                                       | 
     | Welcome to Kepler.B!                                                  | 
     | Your journey starts here!                                             | 
     | To move around in this space use the commands; North, and South       | 
     | To board a ship write; Board. To unboard a ship write; Unboard.       | 
     | All answers must have a capital, eg. "Yes" will work but "yes"        | 
     | will not.                                                             | 
     | ______________________________________________________________________| 
     |/ 
 #doesnt work to optimise but i will make it work then i will do it to the others
  ╱|、_        
 (` - 7      
 |、⁻〵         
 じしˍ,)ノ        

')

print(' ')

print('Current Location; Flight Dock #4, Kepler.B')

print('North: Flight control centre')


print(' ')

print('Where do you want to travel?')
FlightDockDirection = input()

print(' ')

print('Travelling ' + FlightDockDirection)

print(' ')


def typing_effect(text, delay=10):
    """Prints text to the console with a typing effect.

    Args:
        text (str): The text to be printed.
        delay (float, optional): Delay between characters in seconds. Defaults to 0.05.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

# Example usage:
typing_effect("...", delay=0.6)

print(' ')
print(' ')

print('Arrived at the Flight Contril Centre')
print(' ')

door = input(f'The door is locked, do you wish to swipe your card? ')
if door == "Yes":
    print(' ')
    typing_effect("Opening door", delay=0.1)
    print(' ')
if door == "No":
    print(' ')
    typing_effect("Putting Keycard back in pocket", delay=0.1)

print(' ')
print(' ')

print('      ____________________________________________ ')
print('     (                                            |')
print('     | Woah! Look at all these rockets!           |')
print('     | Take a look at them to see where they lead |')
print('     | ___________________________________________|')
print('     |/ ')

print(' ')
print(' ╱|、_        ')
print('(o o  7      ')
print(' |、⁻〵         ')
print(' じしˍ,)ノ         ')

print(' ')


Rocket = input(f'Do you wish to have a look at the rockets? ')
if Rocket == "Yes":
    typing_effect( '  ', delay=0.5)
    print('')
    typing_effect('Hmm, the first rocket seems to be currently under repairs after its journey from Kepler.A', delay=0.1)
    print(" ")
    typing_effect( '  ', delay=0.5)
    typing_effect('The second rocket seems to be ready to leave on a flight course to the asteroid belt', delay=0.1)
    print(" ")
    typing_effect( '  ', delay=0.5)
    typing_effect('And the third rocket seems untouched', delay=0.1)
    print('')
if Rocket == "No":
    print('')
    typing_effect('You back away unsure of the rockets', delay=0.1)

typing_effect( '  ', delay=1.2)
print(" ")

information = input(f'Do you wish to look around ? ')
if information == "No":
    print(" ")
    typing_effect( 'You ignore your surroundings', delay=1)
    print(" ")
if information == "Yes":
    print(' ')
    print(' ')
    information = input (f'You see an information package on the ground, do you wish to read it? ')
    print(' ')
    typing_effect( 'You open the package and a slip of paper falls out;', delay=0.1)
    print(" ")
    typing_effect( '  ', delay=0.5)
    print(" ")
    typing_effect( 'Dr. Barkly;', delay=0.2)
    print(" ")
    typing_effect('"Because we are in space, our North, South, East and West are different compared to those on Earth."', delay=0.1)
    print(" ")
    typing_effect('Instead, we use a universal stellar 2D slice of the solar system and base our North on a bright faraway star."', delay=0.1)
    print("   ")
    print("   ")

    rocketship = input (f'Do you wish to travel? ')
    if rocketship == "No":
        print(" ")
        typing_effect("You stay standing", delay=0.2)
    if rocketship == "Yes":
        print(" ")
        typing_effect("You board the rocketship.", delay=0.2)
        print(" ")
        typing_effect('...', delay=0.2)
        print(" ")
        typing_effect("1..2..3!", delay=0.2)
        print(" ")
        typing_effect('You land on a large not quite spherical body in the asteroid belt', delay=0.2)
        print(" ")
       
        BeltMission = input(f'are you ready to receive your mission? ')
        if BeltMission == "No":
            print(" ")
            typing_effect("Nothing happens", delay=0.2)
            print(" ")
        if BeltMission == "Yes":
            print(" ")
            typing_effect('Incoming call', delay=0.1)
            print(" ")
            typing_effect("...", delay=0.3)
            print(" ")
            print('      ____________________________________________ ')
            print('     (                                            |')
            print('     | Hey! Good to see you again!                |')
            print('     | Here is your mission; Your mission is to   |')
            print('     | catch the rock lizards that live out here  |')
            print('     | They pose a problem so catching them are a |')
            print('     | Priority.                                  |')
            print('     | ___________________________________________|')
            print('     |/ ')
            print(' ')
            print(' ╱|、_        ')
            print('(o o  7      ')
            print(' |、⁻〵         ')
            print(' じしˍ,)ノ         ')
            print(" ")
            print(" ")
            typing_effect("Mission:", delay=0.1)
            typing_effect(" Exterminate the Rock Lizard queen", delay=0.1)
            type_effect("you step off your ship, finally landing of the planet-like asteroid", delay=0.2)


from asteroid import Asteroid

cavern.get_description():

Plains = Asteroid("Plains")
Plains = set_description(" An waste open expanse of grass-like flora.")

Rocket_Pad = Asteroid("Rocket Pad")
Rocket_Pad = set_description(" The Pad holding your rocket however you have not yet completed your mission.")

Research_Facility = Astesroid("Research Facility")
Research_Facility = set_description(" A empty and abandoned shelter.")

Water_Trickles = Asteroid("Water trickles")
Water_Trickles = set_description(" Water flowed through the cracks of stone.")

Mountain = Asteroid("Mountain")
Plains = set_description(" A peak of stone streching into the atmosphere.")

Forested_Area = Asteroid("Forested Area")
Plains = set_description(" A dense ecosystem filled with alien life.")

Landing_Site = Asteroid("Landing Site")
Landing_Site = set_description(" land is lightly burnt due to landing.")

#Landing site
Landing_Site.link_locations(Plains, "North")
Landing_Site.link_locations(Mountain, "West")
Landing_Site.link_locations(Landing_Pad, "East")
#Plains
Plains.link_locations(Landing_Site, "South")
Plains.link_locations(Water_Trickles, "North")
Plains.link_locations(Research_Facility, "East")
Plains.link_locations(West_Trickles, "West")
#Water trickles North
Water_Trickles.link_locations(Plains, "South")
Water_Trickles.link_locations(Mountain, "West")
Water_Trickles.link_locations(Forested_Area, "East")
#Mountain South
Mountain.link_locations(Water_Trickles, "North")
Mountain.link_locations(Landing_Site, "East")
#Water trickles west
Water_Trickles.link_locations(Mountain, "South")
Water_Trickles.link_locations(Mountain, "North")
Water_Trickles.link_locations(Plains, "East")
#Mountain North
Mountain.link_locations(Water_Trickles, "East")
Mountain.link_locations(Water_Trickles, "South")
#Landing_Pad
Landing_Pad.link_locations(Research_Facility, "North")
Landing_Pad.link_locations(Landing_Site, "West")
#Research Facility
Research_Facility.link_locations(Landing_Pad, "South")
Research_Facility.link_locations(Forested_Area, "North")
Research_Facility.link_locations(Plains, "West")
#Forested Area
Forested_Area.link_locations(Research_Facility, "South")
Forested_Area.link_locations(Water_Trickles, "West")




class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        harry = Enemy("Lizard Queen", "The source of the plague")

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

   
    def fight(self, combat_item):
if combat_item == self.weakness:
    print("You fend " + self.name + " off with the " + combat_item )
    return True
else:
    print(self.name + " swallows you, little wimp")
    return False

harry.set_weakness("Electricity")

print("What will you fight with?")
fight_with = input()
harry.fight(fight_with)


class Asteroid:
    def __init__(self, Planet_name):
        self.name = Planet_name
        self.description = None
        self.linked_locations = {}
        self.character = None
        
current_locations = Plains
dead = False
while dead == False:

print("\n")         
    current_cave.get_details()
    # Add your code here
    command = input("> ")    
    current_cave = current_cave.move(command)

inhabitant = current_locations.get_character()
if inhabitant is not None:
    inhabitant.describe()
command = input("<")
current_locations = current_locations.move(command)

elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()

elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                # What happens if you win?
                print("Bravo,hero you won the fight!")
                current_room.set_character(None)
            else:
                print("Scurry back to your ship coward, you lost the fight.")
        else:
            print("There is no one here to fight with")

elif command == "fight":
        ...
        if inhabitant.fight(fight_with) == True:
        else:
            typing_effect("Run away twerp, you lost this fight.",delay=0.2)
            typing_effect("That's the end of the game",delay=0.2)
            dead = True

from character import Character

class Enemy(Character):
    ...  
    def steal(self):
        print("You steal from " + self.name)

class Enemy(Character):
    ...  
    def steal(self):
        print("You steal from " + self.name)

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None
    def pat(self):
        print(self.name + " pats you back!")

Lizard Queen = Enemy("Lizard Queen", "The source of the plague")
Lizard Queen.set_conversation("It's too late to stop it now, you could never win")
Lizard Queen.set_weakness("electricity")
Mountain.set_character(Lizard Queen)
Lesly = Friend("Josephine", "A friendly Lizard")
Lesly.set_conversation("Hey!")
Plains.set_character(Lesly)

elif command == “pat”:
        if inhabitant is not None:
            if instance(inhabitant, Enemy):
                print(“I wouldn’t do that if I were you…")
            else:
                inhabitant.pat()
        else:
            print("There is no one here to pat :(")

class Asteroid:
    def __init__(self, Planet_name):
        ...
        self.item = None
def get_item(self):
    return self.item
def set_item(self, item_name):
    self.item = item_name

def describe(self):
    print ("The [" + self.name + "] is here - " + self.description)

electricity = Item("electricity")
electricity.set_description("The Lizard Queen's weakness")
grotto.set_item(electricity)
Walkie Talkie = Item("walkie talkie")
Walkie Talkie.set_description("A communication device")
dungeon.set_item(Walkie Talkie)

while dead == False:
    item = current_cave.get_item()
    if item is not None:
        item.describe()

Class Item():
    def __init__(self, item_name):
        self.name = item_name
        self.description = None

    def get_name(self):
        return self.name

    def set_name(self, item_name):
        self.name = item.name

    def get_description(self):
        return self.description

    def set_description(self, item_description):
        self.description = item.description

    def describe(self):
        print(
            "The I" + self.name + "I is here - " + delf.description
            )

    Walkie Talkie = Item("Walkie Talkie")
    Walkie Talkie.set_description("A communication device")
    dungeon.set_item(Walkie Talkie)
    bag = []

elif command == "take":
    if item is not None:
      print("You put the " + item.get_name() + " in your bag")
      bag.append(item.get_name())
      current_room.set_item(None)

elif command == "fight":
    if inhabitant is not None and instance(inhabitant, Enemy):
        print("What will you fight with?")
        fight_with = input()
        if fight_with in bag:
            if inhabitant.fight(fight_with) == True:
                print("Bravo hero you have won the fight!")
                current_locations.self_character(None)
                if Enemies.enemies_to_defeat == 0
                        print("Congradulations! You have survived yet another adventure")
                        dead = True
            else:
                print("Scurry back to the rocket, you lost the fight")
                print("That's the end of your game")
                dead = True
        else:
            print("You dont have a " + fight_with)
    else:
        print("There is no one here to fight with")


class Enemy(Character):
    enemies_to_defeat = 0
    def __init__(self, char_name, char_description):
        Enemy.enemies_to_defeat = Enemy.enemies_to_defeat + 1

class Enemy(Character):
    def fight(self, combat_item):
        if combat_item == self.weakness:
            Enemy.enemies_to_defeat = Enemy.enemies_to_defeat - 1
            return True

    enemies_to_defeat = 0
    def __init__(self, char_name, char_description):
        super().__init__(self, char_name, char_description):
        self.weakness = None
        Enemy.enemies_to_defeat = Enemy.enemies_to_defeat + 1

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self)
        return erlf.weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " combat_item)
            Enemy.enemies_to_defeat = Enemy.enemies_to_defeat - 1
            Return True
        else:
            print{self.name + " swallowss you, you little wimp")
            Return False

    def Steal(self)
        print("You steal from " + self.name)

elif command == "fight":
            if inhabitant.fight(fight_with) == True:
                if Enemy.enemies_to_defeat == 0:
                    print("Congratulations, you have survived another adventure!")
                    dead = True


