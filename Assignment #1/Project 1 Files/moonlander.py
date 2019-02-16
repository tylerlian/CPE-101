################################
# CPE 101
# Section: 15
# Project 1: Program
# Name: Tyler Lian
# Cal Poly ID: tklian
################################

# import packages
import sys

# initializing the moonlander class
class Moonlander:
    
    def __init__(self, altitude, fuel):
        self.altitude = altitude
        self.fuel = fuel
        self.velocity = 0
        self.acceleration = 0

    def __repr__(self): 
        return "fuel=" + "(%s)" + ", altitude=" + "(%s)" + ", velocity=" + "(%s)" + ", acceleration=" + "(%s)" % (self.fuel, self.altitude, self.velocity, self.acceleration)

    def __eq__(self, other):
        type(other) == Moonlander
        return self.fuel == other.fuel and self.altitude == other.altitude and self.velocity == other.velocity and self.acceleration == other.acceleration

# displays welcome message
def show_welcome():

    x = print("Welcome to the Moon Lander Simulation!")
    return x

# obtains fuel from user
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

# obtains altitude from user
def get_altitude():

    x = input("Please enter initial altitude [1, 9999]: ")
    
    if(float(x) > 9999 or float(x) < 1) or (x == None):
        if(x == None):
            x = 0
        print(x + " is not a number between 1 and 9999!")
        return get_altitude()
    else:
        altitude = round(float(x), 2)
        return altitude

# displays the state of the moonlander
def display_state(time, altitude, velocity, fuel, fuel_rate):

    x = print("time=" + str(time) + ", altitude=" + str(round(altitude, 2)) + ", velocity=" + str(round(velocity, 2)) + ", fuel=" + str(fuel) + ", fuel rate=" + str(fuel_rate))
    
    return x

# displays when the user has landed and how
def display_landing_status(velocity): 

    if(velocity < 0 and velocity > -1):
        x = print("Status at landing - The eagle has landed!")
        return x
    elif(velocity < -1 and velocity > -10):
        y = print("Status at landing - Enjoy your oxygen while it lasts!")
        return y
    elif(velocity <= -10):
        z = print("Status at landing - Ouch - that hurt!")
        return z

# obtains fuel rate from user
def get_fuel_rate(fuel):

    x = input("Please enter fuel rate [0, 9]: ")

    if(int(x) < 0 or int(x) > 9):
        print(x + " is not a number between 0 and 9!")
        return get_fuel_rate(fuel)
    else:
        fuel_rate = int(x)
        if(fuel - fuel_rate) < 0:
            fuel_rate = fuel
            print("Fuel rate will be changed to: " + str(fuel))
        else:
            print("Fuel rate will be changed to: " + str(fuel_rate))
        return fuel_rate

# updates acceleration for every new time
def update_acceleration(gravity, fuel_rate):
    
    acceleration = gravity * ((float(fuel_rate) / 5.0) - 1)
    acceleration = round(acceleration, 2)
    return acceleration

# updates altitude for every new time
def update_altitude(altitude, velocity, acceleration):

    altitude = altitude + velocity + (acceleration / 2.000)
    altitude = round(altitude, 2)
    return altitude

# updates velocity for every new time
def update_velocity(velocity, acceleration):

    velocity = velocity + acceleration
    velocity = round(velocity, 2)
    return velocity

# updates fuel for every new time
def update_fuel(fuel, fuel_rate):

    if((fuel+1) - (fuel_rate+1)) <= 0:
        fuel_rate = fuel
        fuel = 0
    else:
        fuel = fuel - fuel_rate

    return fuel

# runs all the functions here
def main():

    # Initializes variables
    ml = Moonlander(0, 0)
    time = 0
    gravity = 1.62
    fuel_rate = 0  
    ml.velocity = 0.0
    ml.acceleration = 0.0
    
    
    # Display welcome message
    show_welcome()

    # Gets the altitude
    altitude = get_altitude()

    # Gets the fuel
    fuel = get_fuel()


    ml = Moonlander(altitude, fuel)

    # Will loop until altitude is less than 0
    while(ml.altitude) > 0:
        
        # Updates the Moonlander in a loop until altitude > 0
        display_state(time, ml.altitude, ml.velocity, ml.fuel, fuel_rate)
        fuel_rate = get_fuel_rate(ml.fuel)
        ml.acceleration = update_acceleration(gravity, fuel_rate)
        ml.altitude = update_altitude(ml.altitude, ml.velocity, ml.acceleration)
        ml.velocity = update_velocity(ml.velocity, ml.acceleration)
        ml.fuel = update_fuel(ml.fuel, fuel_rate)
        time += 1

    # When loop ends prints last state and tells the landing status       
    display_state(time, ml.altitude, ml.velocity, ml.fuel, fuel_rate)
    display_landing_status(ml.velocity)	

# Will run if program is run as main file
if __name__ == '__main__':
    main()