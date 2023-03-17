# 1. The Bedroom object has the following attributes:
# • length: length of the room in feet
# • breadth: breadth of the room in feet
# • height: breadth of the room in feet
# • bed: an object representing the bed in the bedroom. Initialize as None.
# • closet: an object representing the closet in the bedroom. Initialize as None.
# • has_balcony: True or False depending on whether the room has a balcony or not
# • has_window: True or False depending on whether the room has a window or not
# • num_lights: The number of lights/lightsockets in the number
# • has_ac: True or False depending on whether the room has a window or not
# • has_fan: True or False depending on whether the room has a window or not
# • num_charging_points: Number of charging points in the room.



# 2. The Bedroom object has the following methods:

# • carpet_area(): Returns the carpet area of the room which is calculated as length*breadth

# • add_bed(): creates a Bed object using user inputs [using input() function] and assigns it to the bed attribute of the bedroom. While adding a bed make sure the dimensions of the bed are suitable for the remaining carpet area in the room.

# For example: you cannot add a 9x9 bed in a 8X10 bedroom
# For example 2: you cannot add a 6x3 bed in a 8x10 bedroom if there is already a closet which takes up 60 sq ft space.

# • add_closet(): creates a Closet object using user inputs [using input() function] and assigns it to the closet attribute of the bedroom. While adding a close make sure the dimensions of the closet are suitable for the remaining carpet area in the room.

# For example: you cannot add a 9x9 closet in a 8X10 bedroom
# For example 2: you cannot add a 6x3 closet in a 8x10 bedroom if there is already a bed which takes up 60 sq ft space.

# • remove_bed(): Checks if the bed attribute is None. If not, then makes it None and returns “bed removed from the room”. If bed attribute is already None, then it returns “No bed found in the room”.

# • remove_closet(): Checks if the closet attribute is None. If not, then makes it None and returns “closet removed from the room”. If closet attribute is already None, then it returns “No closet found in the room”.



import bed
import closet



class Bedroom:

    def __init__(self,length, breadth, heigth, has_balcony,has_window, num_lights,has_ac, has_fan, has_charging_points):
        self.length = int(length)
        self.breadth = int(breadth)
        self.height = heigth
        self.has_balcony = has_balcony
        self.has_window = has_window
        self.num_lights = num_lights
        self.has_ac = has_ac
        self.has_fan = has_fan
        self.has_charging_points = has_charging_points
        self.bed = None
        self.closet = None
  

    def carpet_area(self):
        return (self.length * self.breadth)

 
    def add_bed(self):
        length = input('len of bed:')
        breadth = input('breadth of bed:')
        year = input('enter the year made? ')
        if (year < 2015):
            posts = False
        else:
            posts = input('has posts?')
      
        headboard = input('has head board?')
        material  = input('material')
        self.bed = bed.Bed(length, breadth, year, posts,headboard, material)



  
    def add_closet(self,length, breadth, max_capacity):
        # length = input('length of closet')
        # breadth = input('breadth of closet')
        # max_capacity = input('max_capacity of closet')

        self.closet = closet.Closet(length, breadth, max_capacity)
     

 
    def remove_bed(self):
        if self.bed == None:
            return ('No Bed foundin the room!')
        else:
            self.bed = None
            return ('Bed removed from the room')
    


    def remove_closet(self):
        if self.closet == None:
            return ('No closet found in the room!')
        else:
             self.closet = None
            return ('closet removed from the room')