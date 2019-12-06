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

# Vehicle is the BaseClass
# Two Types of Vehicles 1. Flight Vehicle 2. Ground Vehicle Both should inherit Vehicle
# Two Types of FlightVehicles 1. Starship 2. Airplane Both should inherit FlightVehicle
# Two Types of GroundVehicles 1. Car 2. Motorscycle Both should inherit GroundVehicle

class Vehicle:
    # base class
    pass

class FlightVehicle(Vehicle):
    pass

class GroundVehicle(Vehicle):
    pass

class Starship(FlightVehicle):
    pass

class Airplane(FlightVehicle):
    pass

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

