################################
# CPE 101
# Section: 15
# Project 1: Program
# Name: Tyler Lian
# Cal Poly ID: 015896500
################################

# import packages
import sys

# constant for gravity
gravity = 1.62

class Moonlander:

    def __init__(self, time, altitude, fuel, velocity, acceleration, fuel_rate):
        self.time = time
        self.fuel = fuel
        self.altitude = altitude
        self.velocity = velocity
        self.acceleration = acceleration
        self.fuel_rate = fuel_rate

    def __repr__(self): 
        return "time=" + "(%s)" + ", altitude=" + "(%s)" + ", velocity=" + "(%s)" + ", fuel=" + "(%s)" + ", fuel rate=" + "(%s)" % (self.time, self.fuel, self.altitude, self.velocity, self.fuel, self.fuel_rate)

    def __eq__(self, other):
        type(other) == Moonlander
        return self.fuel == other.fuel and self.altitude == other.altitude and self.velocity == other.velocity and self.acceleration == other.acceleration



def show_welcome():
    x = print("Welcome to the Moon Lander Simulation!")
    return x

def get_fuel():
    x = input("Please enter initial fuel amount [a positive number]: ")
    
    if(int(x) < 1) or (x == None):
        if(x == None):
            x = 0
        print(x + " is not a positive number!")
        x = int(x)
        return get_fuel()
    else:
        fuel = int(x)
        return fuel

def get_altitude():  
    x = input("Please enter initial altitude [1, 9999]: ")
    
    if(float(x) > 9999 or float(x) < 1) or (x == None):
        if(x == None):
            x = 0
        print(x)
        print(x + " is not a number between 1 and 9999!")
        return get_altitude()
    else:
        altitude = round(float(x), 2)
        return altitude

def display_state(time, altitude, velocity, fuel, fuel_rate):    
    x = print("time=" + str(time) + ", altitude=" + str(round(altitude, 2)) + ", velocity=" + str(round(velocity, 2)) + ", fuel=" + str(fuel) + ", fuel rate=" + str(fuel_rate))
    
    return x

def display_landing_status(velocity): 
    x = ""
    if(velocity < 0 and velocity > -1):
        x = print("Status at landing - The eagle has landed!")
    elif(velocity < -1 and velocity > -10):
        x = print("Status at landing - Enjoy your oxygen while it lasts!")
    elif(velocity <= -10):
        x = print("Status at landing - Ouch - that hurt!")

    return x

def get_fuel_rate(fuel):
    x = input("Please enter fuel rate [0, 9]: ")

    if(int(x) < 0 or int(x) > 10):
        print("Value Error: illegal values entered! Please try again!")
        return get_fuel_rate(fuel)
    else:
        fuel_rate = int(x)
        if(fuel - fuel_rate) < 0:
            fuel_rate = fuel
            print("Fuel rate will be changed to: " + str(fuel))
        else:
            print("Fuel rate will be changed to: " + str(fuel_rate))
        return fuel_rate

def update_acceleration(gravity, fuel_rate):
    acceleration = gravity * ((fuel_rate / 5) - 1)
    return acceleration

def update_altitude(altitude, velocity, acceleration):
    altitude = altitude + velocity + float((acceleration / 2))
    return altitude

def update_velocity(velocity, acceleration):
    velocity = velocity + acceleration
    return velocity

def update_fuel(fuel, fuel_rate):
    if((fuel+1) - (fuel_rate+1)) <= 0:
        fuel_rate = fuel
        fuel = 0
    else:
        fuel = fuel - fuel_rate

    return fuel

def main():
    # Intitializes variables
    time = 0
    velocity = 0
    acceleration = 0.0
    fuel_rate = 0
    acceleration = 0
    velocity = 0

    # Display welcome message
    show_welcome()

    # Gets the altitude
    altitude = get_altitude()

    # Gets the fuel
    fuel = get_fuel()


    print(fuel)
    print(altitude)
    while(altitude) > 0:
        display_state(time, altitude, velocity, fuel, fuel_rate)
        acceleration = update_acceleration(gravity, fuel_rate)
        fuel_rate = get_fuel_rate(fuel)
        altitude = update_altitude(altitude, velocity, acceleration)
        velocity = update_velocity(velocity, acceleration)
        fuel = update_fuel(fuel, fuel_rate)
        time += 1   
    display_landing_status(velocity)	

if __name__ == '__main__':
    main()