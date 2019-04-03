""" The test file for Project 4 Crimetime 
CPE 101 
Winter 2019 
Author: Tyler Lian
"""

import crimetime as ct

MONTH = ["January","February", "March", "April", "May", "June", 
        "July","August", "September", "October", "November", "December"]

HOUR = ["1AM", "2AM", "3AM", "4AM", "5AM", "6AM", 
        "7AM", "8AM", "9AM", "10AM", "11AM", "12PM", 
        "1PM", "2PM", "3PM", "4PM", "5PM", "6PM", 
        "7PM", "8PM", "9PM", "10PM", "11PM", "12AM"]

DAY_OF_WEEK = ["MONDAY", "TUESDAY", "WEDNESDAY", \
                "THURSDAY","FRIDAY", "SATURDAY", "SUNDAY"]

class Crime:


    def __init__(self, crime_id, category):
        
        """Initializes object with crime_id and category variables
        
        Args:
            crime_id (int): ID number corresponding to a crime
            category (string): type of crime committed
        
        Returns:
            Crime object created with crime_id and category inputted
        
        """

        self.crime_id = crime_id
        self.category = category
        self.day_of_week = "Day"
        self.month = "Month"
        self.hour = "Hour"
    
    def __eq__(self, other):

        """Checks for equality of self crime_id and other crime_id   
        
        Args:
            self (Crime object): used to compare crime_id
            other (Crime object): used to compare crime_id
        
        Returns:
            (boolean): Equality of the crime_ids
        
        """

        return self.crime_id == other.crime_id

    def __repr__(self):

        """Formats Crime object

        Args:
            self (Crime object): used to obtain crime object variables
        
        Returns:
            Crime object: Formatting of Crime object

        """

        return "(%s)\t(%s)\t(%s)\t(%s)\t(%s)\n" % \
            (self.crime_id, self.category, self.day_of_week, self.month, self.hour)

    def set_time(self, day_of_week, month, hour):
        
        """Updates time variables in crime object to actual variables

        Args:
            day_of_week (string): day of the week crime committed
            month (int): number corresponding to a month
            hour (int): number corresponding to a hour

        Returns:
            Crime object: newly inputted day, month and hour

        """
        
        self.day_of_week = day_of_week
        self.month = MONTH[month-1]
        self.hour = HOUR[hour-1]

crime1 = Crime(1234, "ROBBERY")
crime2 = Crime(2345, "MURDER")
crime3 = Crime(1234, "SHOOTING")

crime1.day_of_week = "SATURDAY"
crime1.month = 8
crime1.hour = 12
crime1.set_time(crime1.day_of_week,crime1.month,crime1.hour)

crime2.day_of_week = "MONDAY"
crime2.month = 3
crime2.hour = 0
crime2.set_time(crime2.day_of_week,crime2.month,crime2.hour)

crime3.day_of_week = "WEDNESDAY"
crime3.month = 6
crime3.hour = 3
crime3.set_time(crime3.day_of_week,crime3.month,crime3.hour)

assert crime1 != crime2
assert crime2 != crime3
assert crime1 == crime3

crimes = list()
crimes.append(crime1)
crimes.append(crime2)
crimes.append(crime3)

lines = ["1234\tROBBERY\tEXPLOSION\n", "2345\tSHOOTING\t12 DEAD\n", "1234\tROBBERY\tEXPLOSION\n"]
assert int(ct.create_crimes(lines)[0].crime_id) == int(crime1.crime_id)
assert int(ct.create_crimes(lines)[0].crime_id) != int(crime2.crime_id)
assert int(ct.create_crimes(lines)[0].crime_id) == int(crime3.crime_id)


assert int(ct.sort_crimes(crimes)[0].crime_id) == int(crime1.crime_id)
assert int(ct.sort_crimes(crimes)[1].crime_id) == int(crime1.crime_id)
assert int(ct.sort_crimes(crimes)[2].crime_id) == int(crime3.crime_id)

crimes_wo_3 = list()
crimes_wo_3.append(crime1)
crimes_wo_3.append(crime3)
times = ["1234\tMONDAY\t05/13/19\t14:05", "2345\tTUESDAY\t06/02/19\t05:13"]
assert ct.update_crimes(crimes_wo_3, times)[0].day_of_week == "MONDAY"
assert ct.update_crimes(crimes_wo_3, times)[1].month == "June"
assert ct.update_crimes(crimes_wo_3, times)[0].hour == "2PM"

assert ct.find_crime(crimes, 1234) == crime1
assert ct.find_crime(crimes, 1234) != crime3
assert ct.find_crime(crimes, 2345) == crime3

"""
All of the functions below cannot be tested with asserts

def read_file(file_name) # reads a file
def write_file(file_name) # writes to a file
def record_file(file_name) # records lines from a file
def write_updated(file_name) # write lines to a file

"""

alist = [1,2,3,4,5,1,1,1]
blist = [2,2,3,4,1,2]
clist = [3,1,2,3,1,3]
assert ct.get_mode(alist) == 1
assert ct.get_mode(blist) == 2
assert ct.get_mode(clist) == 3

assert ct.most_day(crimes) == "MONDAY"
assert ct.most_day(crimes_wo_3) == "MONDAY"
assert ct.most_day(crimes) != "TUESDAY"

assert ct.most_month(crimes) == "May"
assert ct.most_month(crimes_wo_3) == "May"
assert ct.most_month(crimes) != "June"

assert ct.most_hour(crimes) == "2PM"
assert ct.most_hour(crimes_wo_3) == "2PM"
assert ct.most_hour(crimes) != "2AM"