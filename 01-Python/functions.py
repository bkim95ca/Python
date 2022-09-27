from subprocess import CalledProcessError


# Functions WHY?
# RETURN SOMETHING
# CAN BE CALLED
# SAVE SPACE
# REPEATABLE CODE

def function_name(parameter_one, parameter_two):
    pass

a = 59
b = 65
c = a+b
print(c)

a = 90
b = 80
c = a+b
print(c)

def determine_speed(miles, hours):
    print(f"Calculating speed when we travel {miles} miles in {hours} hours")
    # print(miles/hours)
    return(miles/hours)

print(determine_speed(300, 2))