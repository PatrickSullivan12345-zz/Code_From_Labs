#-------------------------------------------------------------------------------
# Name:        Lab 3
# Purpose:
#
# Author:      Patrick Sullivan
#
# Created:     02/02/2018
# Copyright:   (c) patri 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

    #Question 1
    import arcpy
    import math
    import numpy

    arcpy.env.workspace = r"C:\Users\patri\Desktop\Geoprogramming\Lab2_IO"

    if arcpy.Exists("Census_Tracts.shp"):
        print "I did find Census Tracts feature in that folder"
    else:
        print "I did not find it"

    #Question 2
    #A. What’s the value for the variable num after the final iteration?
    #The value of the last iteration num is is 6.
    #B. How many iterations happened during task 4?
    # There were 6 iterations in the duration of the while loop.

    #Task 4
    #while-loop for repeatable jobs
    num = 0
    while num < 6:
        print "The current num Is :" + str(num)
        num = num+1
    else:
        print "The current num is :" + str(num)

    #Question 3
    num2 = 0
    num3 = 0
    while num2 < 10:
        #print num2
        num3 = num3 + num2
        num2 = num2 + 1
    print str(num3)

    #Question 4: FizzBuzz
    number = 3
    if number % 3 == 0 and number % 5 != 0:
        print "Fizz"
    elif number % 3 != 0 and number % 5 == 0:
        print "Buzz"
    elif number % 3 == 0 and number % 5 == 0:
        print "FizzBuzz"
    else:
        print str(number)

    #Question 5
    #Task 6
    # calculate housing price increase
    orig_prices = numpy.array((100, 200, 300))
    rate = 0.1 # yearly increasing rate

    for op in orig_prices:
        op = orig_prices* 0.1

    TotalHousing = op + orig_prices
    print TotalHousing


    """#Task 4
    #While-loop for repeatable jobs
    Num = 0
    while num < 6:
        print "The current num Is :" + str(num)
        num = num+1
    else:
        print "The current num Is :" + str(num)

    #Task 6
    # calculate housing price increase
    orig_price = 100
    rate = 0.1 # yearly increasing rate
    def housing_price(varOrig_price,varRate):
        varOrig_price *= (1+varRate)
        return varOrig_price
    housing_price(orig_price,rate)
    print orig_price"""

if __name__ == '__main__':
    main()
