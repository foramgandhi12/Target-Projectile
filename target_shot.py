#Programmer Name: Foram Gandhi

import math
g = 9.81
pi = math.pi

def get_distance(velocity:float, angle:float)-> float:
    """
    Calculates the distance a projectile travels on a flat surface
    given its intial velocity, and the angle of fire relative
    to the x-axis. The angle is given in radian. This function assumes
    perfect physics, i.e., constant gravity, no air resistance, etc.

    >>> get_distance(0, 1)
    0.0
    >>> get_distance(1, 0)
    0.0
    >>> get_distance(10, 0.25*pi)
    10.19367991845056
    """
    return ((velocity**2)*math.sin(2*angle))/g      #calculates and returns the distance that the projectile travels

def degrees_to_radians(degrees:float)-> float:
    """
    Takes in an angle in degrees, d, and returns an equivalent
    angle in radians

    >>> degrees_to_radians(0)
    0.0
    >>> degrees_to_radians(180)
    3.141592653589793
    """

    return (degrees*(pi/180))       #calculates and returns the angle inputted in degrees to radians

def get_radian_of(angle: str)-> float:
    """
    Takes in a valid input angle_str and returns the numerical value of the
    angle in radians.

    Examples:
    >>> get_radian_of("1.2r")
    1.2
    >>> get_radian_of("45d")
    0.7853981633974483
    """
    if (angle[-1] == "r" or angle[-1] == "R"):     #checks to see if angle given is in radians
        angle = float(angle[0:-1])      #converts angle given as a string into a float
        
    elif (angle[-1] == "d" or angle[-1] == "D"):   #checks to see if angle given is in degrees
        angle = float(angle[0:-1])*(pi/180)     #converts angle given into degrees into angle given in radians and turns tring into a float

    return angle

def is_a_number(string:str)-> bool:
    """
    Returns True if and only if s is a string representing a positive number.

    Examples:
    >>> is_a_number("1")
    True
    >>> is_a_number("One")
    False
    >>> is_a_number("-3")
    False
    >>> is_a_number("3.")
    True
    >>> is_a_number("3.1.2")
    False
    """

    decimals = string.replace(".","",1)     #removes the first occurence of a decimal point
    
    if (decimals.isdigit() == True):    #checks is number is greater than or equal to zero
        if (float(string)>0):    #checks if number is greater than 0
            return True
        else:               #if number is equal to 0 then function returns false
            return False
    else:
        return False

def is_valid_angle(s:str)-> bool:
    """
    Returns True if and only if s is a valid angle. 

    Examples:
    >>> is_valid_angle("85.3d")
    True
    >>> is_valid_angle("85.3.7D")
    False
    >>> is_valid_angle("90d")
    False
    >>> is_valid_angle("0.001r")
    True
    >>> is_valid_angle("1.5R")
    True
    """
    if ((s[0:-1].count('.'))>1):        #checks to see if there is more than one decimal in the input value
        return False 
    
    elif (s[-1] == "d" or s[-1] == "D"):        #checks to see if angle inputed in degrees is valid
        if (float(s[0:-1])>0 and float(s[0:-1])<90):
            return True
        
        else:
            return False
        
    elif (s[-1] == "r" or s[-1] == "R"):        #checks to see if angle inputed in radians is valid
        if (float(s[0:-1])>0 and float(s[0:-1])<(pi/2)):
            return True
        
        else:
            return False
    else:
        return False

def approx_equal(x, y, tol):
    """
    Returns True if and only if x and y are with tol of each other.

    Examples:
    >>> approx_equal(1,2,1)
    True
    >>> approx_equal(4,3,1)
    True
    >>> approx_equal(4,3,0.99)
    False
    >>> approx_equal(-1.5,1.5,3)
    True
    """

    if (abs(x-y) <= tol):       #finds the absolute value of x-y and checks to see if it is less than or equal to the tolerance value
        return True
    else:
        return False


if __name__ == "__main__":
    
    while True:
        target = float(input("Enter a target distance: "))
        tol = float(input("Enter how close you need to be to your target: "))
        target_hit = False
        
        while not target_hit:
            valid_velocity = False

            while not valid_velocity:
                v = input("Enter a valid velocity: ")
                valid_velocity = is_a_number(v)   
            valid_angle = False
            v = float(v)
            
            while not valid_angle:
                theta = input("Enter a valid angle: ")
                valid_angle = is_valid_angle(theta)
            theta = get_radian_of(theta)
            d = get_distance(float(v), theta)
            target_hit = approx_equal(target, d, tol)
            
            if target_hit:
                print("Congratulations! You hit the target.")
            elif target > d:
                print("The shot hit short of the target, try again.")
            else: 
                print("The shot hit past the target, try again.")
            
