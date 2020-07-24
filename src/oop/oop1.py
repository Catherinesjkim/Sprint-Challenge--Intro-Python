# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle: # Base Class for All Vehicles
    pass # Body of base class


class GroundVehicle(Vehicle): # Base Class for All Ground Vehicles
    pass # Body of derived classes

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass


class FlightVehicle(Vehicle): # Base Class for All Fling Vehicles
    pass # Body of derived class

class Airplane(FlightVehicle):
    pass


class Starship(FlightVehicle): # Base Class for All Flying Space Vehicles
    pass