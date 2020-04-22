#!/usr/bin/env python   
#the above just indicates to use python to intepret this file

import sys             #a python module with system functions for this OS

# ------------------------------------------------------------
#  this 'for loop' will set 'line' to an input line from system 
# ------------------------------------------------------------
for line in sys.stdin:  
#-----------------------------------
#sys.stdin call 'sys' to read a line from standard input, 
# note that 'line' is a string object, ie variable, and it has methods that you can apply to it,
# as in the next line
# ---------------------------------
    line = line.strip()  #strip is a method, ie function, associated
                         #  with string variable, it will strip 
                         #   the carriage return (by default)
    keys = line.split()  #split line at blanks (by default), 
                         #   and return a list of keys
    for key in keys:     #a for loop through the list of keys
        value = 1        
        print('{0}\t{1}'.format(key, value) )
