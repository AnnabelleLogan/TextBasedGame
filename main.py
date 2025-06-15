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


cavern.link_locations(dungeon, "south")
cavern.link_locations(dungeon, "south")
cavern.link_locations(dungeon, "south")
cavern.link_locations(dungeon, "south")
cavern.link_locations(dungeon, "south")
cavern.link_locations(dungeon, "south")
cavern.link_locations(dungeon, "south")
#etc.


current_locations = Plains          
while True:		
    print("\n")         
    current_cave.get_details()         
    command = input("> ")    
    current_cave = current_cave.move(command) 

harry = Enemy("Harry", "A smelly Wumpus")
harry.set_conversation("Hangry…Hanggrry")
harry.set_weakness("vegemite")


class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        harry = Enemy("Harry", "A smelly Wumpus")

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

harry.set_weakness("vegemite")

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

inhabitant = current_cave.get_character()
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
                print("Scurry home, you lost the fight.")
        else:
            print("There is no one here to fight with")

elif command == "fight":
        ...
        if inhabitant.fight(fight_with) == True:
        else:
            print("Scurry home, you lost the fight.")
            print("That's the end of the game")
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

harry = Enemy("Harry", "A smelly Wumpus")
harry.set_conversation("hangryyy. Hungryyy..")
harry.set_weakness("vegemite")
Mountain.set_character(harry)
josephine = Friend("Josephine", "A friendly bat")
josephine.set_conversation("Gidday")
grotto.set_character(josephine)

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

vegemite = Item("vegemite")
vegemite.set_description("A Wumpuses worst nightmare")
grotto.set_item(vegemite)
torch = Item("torch")
torch.set_description("A light for the end of the tunnel")
dungeon.set_item(torch)

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

    torch = Item("Torch")
    torch.set_description("A light for the end of the tunnel")
    dungeon.set_item(torch)
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

        
        
        
        



    

    











