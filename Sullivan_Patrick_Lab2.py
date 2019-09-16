#-------------------------------------------------------------------------------
# Name:        Patrick Sullivan
# Purpose:     Homework Lab 2
#
# Author:      Patrick
#
# Created:     31/01/2018
# Copyright:   (c) patri 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass


    import os
    import arcpy

    path = r'C:\Users\patri\Desktop\Geoprogramming\Lab2_IO'

    #Question 1
    #How to write a file by appending new lines into the file:
    myResponse = raw_input("Please write something")
    StringValue = str(myResponse)

    file = open(path + r'\test.txt', "a+")
    file.write( "\n" + "\n" + myResponse) #write text in the file

    try:
        file = open(path + r'\test.txt', "r")
        data = file.read()
        print data
    except Exception as e:
        print e
    finally:
        file.close()

    #Question 2
    #Extending from task 5, create a Python script that will write an list of
    #feature class names from the folder Lab2\_IO sorted by alphabetical order
    #into a new text file
    arcpy.env.workspace = "C:\Users\patri\Desktop\Geoprogramming\Lab2_IO"
    fcList= arcpy.ListFeatureClasses("*")

    fcList.sort()
    File2 = open("Lab2.txt" , "w+")

    count = 1

    for fc in fcList:
        File2.write("File " + str(count) + ": " + fc + "\n")
        count = count + 1

    File2.close()

    #Question 3
    #Write a Python program to sum all the items in the list [100,200,300, 500]
    list = [100,200,300, 500]

    sum = 0

    for combine in list:
        sum += combine

    print sum

    #Question 4
    #Write a Python program to count the number of characters in a string using
    #the dictionary data type
    #Input: Google.com
    #Output: ?o?: 3, ?g?: 2, ?.?: 1, ?e?: 1, ?l?: 1, ?m?: 1, ?c?: 1
    #LetterCount =0
    string = "google.com"
    def letter_counter(string):
        list2 = {}
        for letter in string:
            count2 = list2.keys()
            if letter in count2:
                list2[letter] += 1
            else:
                list2[letter] = 1
        return list2
    print(letter_counter(string))

if __name__ == '__main__':
    main()
