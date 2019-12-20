# Deidra Driscoll
# Software Development Fundementals
# Programming_lab_9, This is a program that manages a collection of drones and their positions. This program is also object-oriented wih two class: Drone and DroneController. Drone will maintain information about each drone, and provide functionality for moving, displaying and getting the distance between another drone. DroneController will listen for user input to manipulate and view a collection of Drone objects.

# Import json
import json
# Import math
import math

from flask import render_template

# Define class Drone
class Drone:
    """Maintain information about each drone
    attrubutes: x and y
    """

    # Create attrubutes in constructor (self is name, self.x is x, self.y is y)
    def __init__(self, x: int, y: int):
        self.x = int(x)
        self.y = int(y)

    # Create method to move drone
    def move_drone(self, deltaX, deltaY):
        # Add deltaX and deltaY to the x and y variable for self
        self.x += deltaX
        self.y += deltaY
        # Convert int to  str
        x = str(self.x)
        y = str(self.y)
        # Create location value
        location = (x + " , " + y)
        # Return location value
        return location

    # Create method to print drone ##############################
    def print_drone(self):
        x = self.x
        y = self.y
        x = str(x)
        y = str(y)
        str_xy = (x + " , " + y)
        value_print = str(": " + str_xy)
        return value_print

    # Create method to get distance
    def get_distance(self, second_drone):
        # Create empty dictionary
        drones = {}
        # Open json file to upload dictionary
        with open("drones.json", "r") as f:
            # Load key-value pairs
            dictionary_from_file = json.load(f)
            for name_of_drone, location in dictionary_from_file.items():
                # Update drones dictionary
                drones[name_of_drone] = location
        # Validate that the name of drones 2 exists
        if second_drone in drones:
            # Make location_2 equal to the name_of_drones_2-value pair
            location_2 = drones[second_drone]
            # Make x and y variable
            location_2 = location_2.split(" , ")
            # Create x and y variable
            for XandY in range(len(location_2)):
                if XandY is 0:
                    x_2 = int(location_2[XandY])
                if XandY is 1:
                    y_2 = int(location_2[XandY])
            drone_2 = Drone(x_2, y_2)
            # Calculate distance between first choice and second
            distance = math.sqrt(((self.x - x_2) ** 2) + ((self.y - y_2) ** 2))
            return distance
        # If it does not then print why
        if second_drone not in drones:
            return "Drone not found"


# Define ClassController
class DroneController:
    # No attributes in constructor
    def __init__(self):
        pass

    # Define main function


    # Define dictionary
    def drone_dict(self):
        # Create empty dictionary
        drones = {}
        # Create try exception handling
        try:
            # Open and read json file
            with open("drones.json", "r") as f:
                # Load key-value pairs
                dictionary_from_file = json.load(f)
                # Establish key-value pairs in the file from dictionary
                for name_of_drone, location in dictionary_from_file.items():
                    # Update dictionary
                    drones[name_of_drone] = location
            # return dictionary
            return drones
        # If filenotfounderror, then create new json file
        except FileNotFoundError:
            print("Error reading file. Please try again.")
            with open("drones.json", "w") as f:
                json.dump(drones, f, indent=2)
            quit()


    # Define add_drone
    def add_drone(self, name_of_drone):
        # Call and set dictionary equal to drones
        drones = self.drone_dict()
        ####
        # Validate that name_of_drone is not in drones dictionary
        if name_of_drone not in drones:
            # Set location value
            location = "0 , 0"
            # Update drones dictionary
            drones[name_of_drone] = location
            # Print new dictionary to new file
            with open("drones.json", "w") as f:
                json.dump(drones, f, indent=2)
            # Create x and y values
            location = location.split(" , ")
            # Set x and y
            for XandY in range(len(location)):
                if XandY is 0:
                    x = int(location[XandY])
                if XandY is 1:
                    y = int(location[XandY])
            drone_1 = Drone(x, y)
            string = drone_1.print_drone()
            new_drone_name = str(name_of_drone + string)
            return new_drone_name
        if name_of_drone in drones:
            exist = "Drone already exists"
            return exist


    def move_drone(self, drone_to_move, move_x, move_y):
        # Call and set dictionary equal to drones
        drones = self.drone_dict()
        # Validate drone name exists
        if drone_to_move in drones:
            # Create location value
            location = drones[drone_to_move]
            # Create x and y values
            location = location.split(" , ")
            # Set x and y
            for XandY in range(len(location)):
                if XandY is 0:
                    x = int(location[XandY])
                if XandY is 1:
                    y = int(location[XandY])
            # Make drone equal to the x,y value
            drone = Drone(x, y)
            # Create values to add to the drone
            # Set location equal to the new value
            location = drone.move_drone(move_x, move_y)
            # Make name_of_drone equal to the new updated location
            drones[drone_to_move] = location
            # Update json file
            with open("drones.json", "w") as f:
                json.dump(drones, f, indent=2)
            drones = self.drone_dict()
            # Call and set dictionary equal to drones
            # Create item pairs
            drone_item = drones.items()
            # Set name_of_drone, location as key, value pair in drone_items
            for name_of_drone, location in drone_item:
                # Create x and y values
                location = location.split(" , ")
                # Set x and y values
                for XandY in range(len(location)):
                    if XandY is 0:
                        x = int(location[XandY])
                    if XandY is 1:
                        y = int(location[XandY])
                # Print drone info
                print(name_of_drone + ":", x, ",", y)

        if drone_to_move not in drones:
            return "move_drone_not_found"

    def drone_distance(self, first_drone, second_drone):
        # Call and set dictionary equal to drones
        drones = self.drone_dict()
        # Establish first drone name

        # Validate if drone is in dictionary
        if first_drone in drones:
            # Set location_1 equal to value of name_of_drone_1
            location_1 = drones[first_drone]
            # Create x and y values
            location_1 = location_1.split(" , ")
            for XandY in range(len(location_1)):
                if XandY is 0:
                    x_1 = int(location_1[XandY])
                if XandY is 1:
                    y_1 = int(location_1[XandY])
            # Create drone_1 equal to class Drone with the same x and y variables as name_of_drone_1
            drone_1 = Drone(x_1, y_1)
            # Get distance
            dist = drone_1.get_distance(second_drone)
            return dist
        if first_drone not in drones:
            return "First Drone not found"

    # Create display for all drones
    def display_drones(self):
        # Call and set dictionary equal to drones
        drones = self.drone_dict()
        # Create item pairs
        drone_item = drones.items()

        drone_display = []
        # Set name_of_drone, location as key, value pair in drone_items
        for name_of_drone, location in drone_item:
            # Create x and y values
            location = location.split(" , ")
            # Set x and y values
            for XandY in range(len(location)):
                if XandY is 0:
                    x = int(location[XandY])
                if XandY is 1:
                    y = int(location[XandY])
            # Print drone info
            display = (name_of_drone + ":", x, ",", y)
            drone_display.append(display)

