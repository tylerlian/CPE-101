### CPE 101 : Project 1 ###

import sys

#constant for gravity
GRAVITY = 1.62

class Moonlander:
    '''This is a class for maintaing the state of the moonlander.
    The moonlander class has following fields (attributes).

    Attributes:
        fuel (int): fuel in the moonlander
        altitude (float): altitude of the moonlander
        velocity (float): velocity of the moonlander
        accel (float): acceleration of the moonlander
    '''
    def __init__(self, altitude, fuel):
        '''constructor of Moonlander object.
        It initializes fuel, altitude, velocity, and accel attributes.

        Args:
            fuel (int): initial(original) fuel
            altitude (float): initial(original) altitude

        Returns:
            object(Moonlander): Moonlander object
                                   with its attributes initialized.
        '''
        #to-do: comment out the next 4 lines and initialize each member variable
        #self.fuel = 
        #self.altitude = 
        #self.velocity = 
        #self.accel =
        #remove the 'pass' line after completing this method.
        pass

    ### Implement other two boiler plate methods here ###



def show_welcome():
    '''[Replace this line with the purpose of this function.]
   
    Args:
        None

    Returns:
        None
    '''
    #to-do: remove the 'pass' and implement this function.
    pass

def get_fuel():
    '''[Replace this line with the purpose of this function.]
   
    Args:
        None

    Returns:
        None
    '''
    #to-do: remove the 'pass' and implement this function.
    pass

def get_altitude():
    '''[Replace this line with the purpose of this function.]
   
    Args:
        None

    Returns:
        None
    '''
    #to-do: remove the 'pass' and implement this function.
    pass

def display_state(time, altitude, velocity, fuel, fuel_rate):
    '''to-do: Replace this line with the purpose of this function.
   
    Args:
        time(int): 
        altitude (float): altitude of the moonlander
        velocity (float): velocity of the moonlander
        fuel (int): fuel in the moonlander
        fuel_rate (int): fuel consumption rate 

    Returns:
        None
    '''
    #to-do: remove the 'pass' and implement this function.
    pass

def display_landing_status(velocity):
    '''to-do: Replace this line with the purpose of this function.
   
    Args:
        velocity (float): velocity of the moonlander

    Returns:
        None
    '''
    #to-do: remove the 'pass' and implement this function.
    pass

def get_fuel_rate(fuel):
    '''to-do: Replace this line with the purpose of this function.
   
    Args:
        fuel (int): fuel in the moonlander

    Returns:
        int: fuel rate 
    '''
    #to-do: remove the 'pass' and implement this function.
    pass

def update_acceleration(gravity, fuel_rate):
    '''to-do: Replace this line with the purpose of this function.
   
    Args:
        gravity (float): gravity
        fuel_rate (int): fuel consumption rate 

    Returns:
        float: updated acceleration 
    '''
    #to-do: remove the 'pass' and implement this function.
    pass

def update_altitude(altitude, velocity, acceleration):
    '''to-do: Replace this line with the purpose of this function.
   
    Args:
        altitude (float): altitude of the moonlander
        velocity (float): velocity of the moonlander
        acceleration (float): fuel in the moonlander

    Returns:
        float: updated altitude 
    '''
    #to-do: remove the 'pass' and implement this function.
    pass

def update_velocity(velocity, acceleration):
    '''to-do: Replace this line with the purpose of this function.
   
    Args:
        velocity (float): velocity of the moonlander
        acceleration (float): fuel in the moonlander

    Returns:
        float: updated velocity 
    '''
    #to-do: remove the 'pass' and implement this function.
    pass

def update_fuel(fuel, fuel_rate):
    '''to-do: Replace this line with the purpose of this function.
   
    Args:
        fuel (int): fuel in the moonlander
        fuel_rate (int): fuel consumption rate 

    Returns:
        int: updated fuel amount 
    '''
    #to-do: remove the 'pass' and implement this function.
    pass 

def main():
    '''This is your main function which drives the simulation.
    All function calls are made in this function.
   
    Args:
        None

    Returns:
        None 
    '''
    #to-do: remove the 'pass' and implement this function.
    pass

if __name__ == '__main__':
    #main() function above will be called when this file is the top level code.
    main()
