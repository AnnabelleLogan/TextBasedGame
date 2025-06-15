class Asteroid():
    def __init__(self, Planet_name):
        self.name = Planet_name
        self.description = None
        self.linked_locations = {}

    def set_description(self, Planet_description)
        self.description = Planet_description

    def get_decription(self):
        return self.description
    
    def set_name(self, Planet_nane):
        self.name = Planet_name

    def get_name(self):
        return self.name

    def set_character(self, new_character):
        set.character = new_character

    def get_character(self):
        return selt.character

    def describe(self):
        print(self.description)

    def link_locations(self, locations_to_link, direction):
        self.linked_locations[direction] = locations_to_link

    def get_details(self):
        print(self.name)
        print("----------")
        print(self.description)
        for direction in self.linked_locations:
            locations = self.linked_locations[direction]
            print{"The " + locations.get_name() + " is " + direction)
        



    
    def get_description(self, Planet_name):
        return self.description
    def describe(self):
        print( self.description )
    

    def __init__(self, Planet_name):
        self.linked_caves = {}

    print( self.name + " linked locations :" + repr(self.linked_locations) )

    def link_locations(self, locations_to_link, direction):
        self.linked_locations[direction] = locations_to_link
        

    def get_details(self):
    for direction in self.linked_locations:
        locations = self.linked_locations[direction]
        print( "The " + locations.get_name() + " is " + direction)


    def move(self, direction):
    if direction in self.linked_locations:
        return self.linked_locations[direction]
    else:
        print("You can't go that way")
        return self




    



    
