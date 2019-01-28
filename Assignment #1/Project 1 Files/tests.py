################################
# CPE 101
# Section: 15
# Project 1: Tests
# Name: Tyler Lian
# Cal Poly ID: 015896500
################################

# imports moonlander.py and Moonlander class from moonlander.py
import moonlander as moonlander
from moonlander import Moonlander

# initialized variables
gravity = 1.62
time = 0
fuel_rate = 0
ml = Moonlander(0,0)
ml.velocity = 0.0
ml.acceleration = 0.0


# cannot be tested as they are user input
moonlander.show_welcome()
altitude = moonlander.get_altitude()
fuel = moonlander.get_fuel()
ml = Moonlander(altitude, fuel)
print(ml.fuel)
fuel_rate = moonlander.get_fuel_rate(ml.fuel)
print(fuel_rate)

# displays format of program
moonlander.display_state(time, ml.altitude, ml.velocity, ml.fuel, fuel_rate)

# tests for landing status
x = print("Status at landing - The eagle has landed!")
y = print("Status at landing - Enjoy your oxygen while it lasts!")
z = print("Status at landing - Ouch - that hurt!")

assert moonlander.display_landing_status(-.5) == x
assert moonlander.display_landing_status(-5) == y
assert moonlander.display_landing_status(-50) == z

# tests for acceleration
assert moonlander.update_acceleration(gravity, 0) == -1.62
assert moonlander.update_acceleration(gravity, 5) == 0
assert moonlander.update_acceleration(gravity, 9) == 1.30

# tests for altitude
assert moonlander.update_altitude(1500, -18.52, -1.62) == 1480.67
assert moonlander.update_altitude(2700, 18.51, 3.41) == 2720.22
assert moonlander.update_altitude(1551, -21.43, -5.41) == 1526.87

# tests for velocity
assert moonlander.update_velocity(-18.52, -1.62) == -20.14
assert moonlander.update_velocity(18.51, 3.41) == 21.92
assert moonlander.update_velocity(-21.43, -5.41) == -26.84

# tests for fuel
assert moonlander.update_fuel(10, 9) == 1
assert moonlander.update_fuel(10, 5) == 5
assert moonlander.update_fuel(20, 13) == 7


