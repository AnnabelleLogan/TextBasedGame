class Asteroid():
    def __init__(self, Planet_name):
        self.name = Planet_name
        self.description = None
    def get_description(self, Planet_name):
        return self.description
    def describe(self):
        print( self.description )
    

    def __init__(self, Planet_name):
        self.linked_caves = {}

    print( self.name + " linked locations :" + repr(self.linked_locations) )

    def link_locations(self, locations_to_link, direction):
        self.linked_locations[direction] = locations_to_link
        


    



    
