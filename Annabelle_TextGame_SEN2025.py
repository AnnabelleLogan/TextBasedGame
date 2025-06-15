
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





print('      _______________________________________________________________________')
print('     (                                                                       |')
print('     | Welcome to Kepler.B!                                                  |')
print('     | Your journey starts here!                                             |')
print('     | To move around in this space use the commands; North, and South       |')
print('     | To board a ship write; Board. To unboard a ship write; Unboard.       |')
print('     | All answers must have a capital, eg. "Yes" will work but "yes"        |')
print('     | will not.                                                             |')
print('     | ______________________________________________________________________|')
print('     |/ ')
print(' ')
print('  ╱|、_        ')
print(' (` - 7      ')
print(' |、⁻〵         ')
print(' じしˍ,)ノ         ')

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

class Aesteroid():
    def __init__(self, Planet_name):
        self.name = Planet_name
        self.description = None

    def get_description(self):
        return self.description

    def set_description(self, Asteroid_description):
        self.description = Asteroid_description

    def set_description(self, Asteroid_description):
        self.description = Asteroid_description




# if curiosity == "No":
#     print('You stand there awkwardly')

# https://rosettacode.org/wiki/Hunt_the_Wumpus
