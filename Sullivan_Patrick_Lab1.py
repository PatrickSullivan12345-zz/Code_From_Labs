#-------------------------------------------------------------------------------
# Name:        Lab 1
# Purpose:
#
# Author:      pps7
#
# Created:     30/01/2018
# Copyright:   (c) pps7 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():

    #Homework
    #Question 2.1
    import arcpy #import arcpy tools

    arcpy.env.workspace = "C:/Users/pps7/Desktop/Lab1_Python"
    #Imports data from the data from the data's location in the computer.

    #The "ListFeatureClasses" uses a set of keywords to operate. More at:
    #https://anothergisblog.blogspot.com/2011/05/listing-data-with-arcpy.html
    fcList = arcpy.ListFeatureClasses( "*", "Polygon")

    #Establishes the variable fc and filters through the variable "fcList" and
    #it looks for the polygon classes.
    for fc in fcList:
        print fc  #Shows output.

    print "     " #Break between problems.

    #Question 2.2
    arcpy.env.workspace = "C:/Users/pps7/Desktop/Lab1_Python"
    fcList = arcpy.ListFeatureClasses()
    List2 = [] #Create new list.

    for fc in fcList: #Create a filter to count the numbers in the new list
        List2.append(fc) # with a for-loop

    Total_Number = len(List2) #Counts the length of the string.

    print Total_Number #Prints the length.

if __name__ == '__main__':
    main()