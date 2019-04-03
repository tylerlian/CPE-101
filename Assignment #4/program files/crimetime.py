"""The module file for Project 4 Crimetime
CPE 101
Winter 2019
Author: 
    Tyler Lian
"""
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

def create_crimes(lines):
    
    """Creates a crime object list

    Args: 
        lines (list): a list of Crime objects   

    Returns:         
        Crime object: A Crime object corresponding to the crime_id.

    """

    array = []
    counter = 0

    for line in lines:
        found = 0
        string = line.split("\t")
        try:
            if string[1] == "ROBBERY":
            
                for counter in range(len(array)):
                    if array[counter].crime_id == string[0]:
                        found = 1
                if found != 1:
                    array.append(Crime(string[0],string[1]))
        except:
            pass
        
    return array

def sort_crimes(crimes):
    
    """Selection sorts crimes based on crime id      

    Args: 
        crimes (list): a list of Crime objects   

    Returns:         
        crimes (list): sorted list by crime_id

    """

    length = len(crimes)
    for crime in range(length):
        minimum = crime

        for ids in range(crime+1, length):

            if int(crimes[minimum].crime_id) > \
                int(crimes[ids].crime_id):
                minimum = ids

        temp = crimes[crime].crime_id
        crimes[crime].crime_id = crimes[minimum].crime_id 
        crimes[minimum].crime_id = temp

    return crimes

def update_crimes(crimes, lines):
    
    """Finds a crime from a crime id.  

    Args: 
        crimes (list): a list of Crime objects         
        lines (list): a list of Crime times

    Returns:         
        Crime object: updated day, month and hour

    """

    length = len(lines)
    for line in range(length):
        string = lines[line].split("\t")
        location = find_crime(crimes, string[0])
        try:
            location.day_of_week = string[1]
            location.month = int(string[2][0:2])
            location.hour = int(string[3][0:2])
            location.set_time(location.day_of_week, \
                location.month,location.hour)
        except:
            pass

    return crimes

def find_crime(crimes, crime_id):
    
    """Finds a crime from a crime id.       
    
    Args: 
        crimes (list): a list of Crime objects         
        crime_id (int): a crime id number
    
    Returns:         
        Crime object: A Crime object corresponding to the crime_id.
    
    """

    beg = 0
    end = len(crimes)-1
    # print(crimes)
    while beg != end:

        midpoint = (beg + end)//2
        # print(beg, end, midpoint)
        if int(crimes[midpoint].crime_id) == int(crime_id):
            return crimes[midpoint]
        elif int(crime_id) < int(crimes[midpoint].crime_id):
            end = midpoint
        elif int(crime_id) > int(crimes[midpoint].crime_id):
            beg = midpoint+1
    if int(crimes[end].crime_id) == int(crime_id):
        return crimes[end]
    return None

def read_file(file_name):

    """Opens file name as readable      
    
    Args: 
        file_name (string): name of file user wants to read
    
    Returns:         
        File variable (string): creates variable out of file name
    
    """

    file = open(file_name, 'r')
    file.readline()

    return file

def write_file(file_name):

    """Opens file name as writable      
    
    Args: 
        file_name (string): name of file user wants to write on
    
    Returns:         
        File variable (string): creates variable out of file name
    
    """

    file = open(file_name, 'w')
    file.write("ID\tCategory\tDayOfWeek\tMonth\tHour\n")

    return file

def record_file(file_name):
    
    """Appends all lines in a file onto a list      
    
    Args: 
        file_name (string): file_name user wants to record lines of
    
    Returns:         
        Array (list): includes all lines in the file
    
    """

    array = list()
    line = True
    array = file_name.readlines()
    return array

def write_updated(updated, file_name):
    
    """Print information from updated class "Crime" onto file_name     
    
    Args: 
        updated (list): list of "Crime" objects
        file_name (string): file_name user wants to write lines on
    
    Returns:         
        None
    
    """

    length = len(updated)
    for counter in range(length):
        file_name.write(updated[counter].crime_id + "\t" + \
            updated[counter].category + "\t" + \
            updated[counter].day_of_week + "\t" + \
            updated[counter].month + "\t" + \
            updated[counter].hour + "\n")
    return

def get_mode(alist):

    """Find most common occurance in a list     
    
    Args: 
        alist (list): a list of values      
    
    Returns:         
        (int or string): Variable that most commonly occurs in alist
    
    """

    temp = list()
    max_count = 0
    index = 0
    for counter in range(len(alist)):
        count = alist.count(alist[counter])
        if count > max_count:
            max_count = count
            index = counter
    return alist[index]

def most_day(updated):

    """Finds most commonly occuring day       
    
    Args: 
        updated (list): list of "Crime" objects
    
    Returns:         
        day_of_week (string): Most commonly occuring day in "updated"
    
    """

    alist = list()
    length = len(updated)
    for counter in range(length):
        alist.append(updated[counter].day_of_week)
    return get_mode(alist)

def most_month(updated):

    """Finds most commonly occuring month    
    
    Args: 
        updated (list): list of "Crime" objects
    
    Returns:         
        month (string): Most commonly occuring month in "updated"
    
    """

    alist = list()
    length = len(updated)
    for counter in range(length):
        alist.append(updated[counter].month)
    return get_mode(alist)

def most_hour(updated):

    """Finds most commonly occuring hour    
    
    Args: 
        updated (list): list of "Crime" objects
    
    Returns:         
        hour (string): Most commonly occuring hour in "updated"
    
    """

    alist = list()
    length = len(updated)
    for counter in range(length):
        alist.append(updated[counter].hour)
    return get_mode(alist)

def main():

    """Runs program     
    
    Args: 
        None
    
    Returns:         
        None
    
    """

    crime = read_file("crimes.tsv")
    time = read_file("times.tsv")
    rob = write_file("robberies.tsv")
    lines = record_file(crime)
    crimes = create_crimes(lines)
    crimes = sort_crimes(crimes)
    lines = record_file(time)
    updated = update_crimes(crimes, lines)
    write_updated(updated, rob)

    print("NUMBER OF PROCESSED ROBBERIES: %d" % (len(updated)-1))
    print("DAY WITH MOST ROBBERIES: %s" % most_day(updated))
    print("MONTH WITH MOST ROBBERIES: %s" % most_month(updated))
    print("HOUR WITH MOST ROBBERIES: %s" % most_hour(updated))

if __name__ == "__main__":

    main()
    