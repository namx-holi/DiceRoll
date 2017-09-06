#!/usr/bin/python3

"""
Rolling Dice

Call with argument as being the dice

i.e. roll 4d6 - 4
"""

# if this is being launched with python3, rename input to
# raw_input. this should always be the case, but if this
# is launched with python2 it should still work this way.
try:
    raw_input
except:
    raw_input=input


# imports
from sys import argv, stdout
from random import randint


# method for rolling a single n-sided die
def roll_die(arg):
    
    # if the arg is empty, just return 0
    if arg is "":
        return 0
    
    # if there is no 'd' in the argument, assume the
    # argument is "rolling" a constant
    if "d" not in arg:
        return int(arg)
    
    # if the first character of the argument is '-',
    # we need to negate the final answer.
    if arg[0] is "-":
        is_negative = True
        # because negative, remove the first character
        # (ie remove the - so it can be parsed)
        arg = arg[1:]
    else:
        is_negative = False
    
    # split the number of rolls and the number of sides
    rolls, sides = arg.split("d")
    
    # if the number of rolls isnt specified, assume it
    # is one roll of the die
    if rolls:
        rolls = int(rolls)
    else:
        rolls = 1
    
    # init total and roll the die the number of times
    # required and add to total
    total = 0
    for roll in range(rolls):
        total += randint(1, int(sides))
    
    # if this total was meant to be negative, multiply
    # the total by -1
    if is_negative:
        total *= -1
    
    # finally, return the calculated total.
    return total


# method for rolling all the dice
def roll(arg):
    
    # get a list of individual dice rolls to roll
    dice_rolls = arg.replace(" ","").replace("-","+-").split("+")
    
    # for each die, roll it using the previously defined
    # method and add the result to the total
    total = 0
    for roll in dice_rolls:
        total += roll_die(roll)
    
    # finally, return the total
    return total


# method to be run when this is called from command line
def main():
    
    # check if there were any arguments
    # this is >1 since the call 'roll' is considered
    # an argument (thanks python?)
    if len(argv) > 1:
        # join all the arguments together to make
        # one string to be used to roll
        roll_arg = "".join(argv[1:])
        
        # roll these dice and get the total
        roll_total = roll(roll_arg)
        
        # display the rolled total
        stdout.write("You rolled a %s!\n" % roll_total)
    
    # if there were no arguments, ask the user to call
    # this again but with arguments
    else:
        stdout.write("No dice? Please try again.\n")


# call the main method!
main()
