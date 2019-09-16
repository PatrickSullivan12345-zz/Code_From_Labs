#-------------------------------------------------------------------------------
# Name:        Lab10
# Purpose:
#
# Author:      Patrick O'Sullivan
#
# Created:     27/03/2018
# Copyright:   (c) patri 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

    """
    Pseudocode
    1. Get sun position from http://aa.usno.navy.mil/data/docs/AltAz.php
    2. Save data to excel
    3. Convert excel to table conversion
    4. set new variable for total hour and other parameters for hillshade
    5. To create the mean solar radiation raster make a search cursor that:
        (For loop 1)
            5.1 compute total hour
            5.2 also the parameters for hillshade, (altitude = row[1])
            5.3 Compute hillshade for each hour
            5.4 Add the rasters that are in the day time (solar)
        create a new list to store solar
    6. for loop 2 (for items in solar list)
        6.1 add all raster
        6.2 Find the average
    7. Create a map.
    """

    import arcpy
    from arcpy import env
    from arcpy.sa import *

    import csv
    import io

    #Opening csv files: https://docs.python.org/2/library/csv.html

    with open("Lab_10_Data.csv","rb") as File:
        reader = csv.reader(File)
        for row in reader:
            if row[1] == "-8.8":
                A1 = row[1]
                Alitude1 = float(A1)
            elif row[1] == "4.4":
                A2 = row[1]
                Alitude2 = float(A2)
            elif row[1] == "17.2":
                A3 = row[1]
                Alitude3 = float(A3)
            elif row[1] == "29.7":
                A4 = row[1]
                Alitude4 = float(A4)
            elif row[1] == "41.5":
                A5 = row[1]
                Alitude5 = float(A5)
            elif row[1] == "51.6":
                A6 = row[1]
                Alitude6 = float(A6)
            elif row[1] == "58.3":
                A7 = row[1]
                Alitude7 = float(A7)
            elif row[1] == "59.4":
                A8 = row[1]
                Alitude8 = float(A8)
            elif row[1] == "54.2":
                A9 = row[1]
                Alitude9 = float(A9)
            elif row[1] == "44.9":
                A10 = row[1]
                Alitude10 = float(A10)
            elif row[1] == "33.6":
                A11 = row[1]
                Alitude11 = float(A11)
            elif row[1] == "21.3":
                A12 = row[1]
                Alitude12 = float(A12)
            elif row[1] == "8.5":
                A13 = row[1]
                Alitude13 = float(A13)
            elif row[1] == "-4.6":
                A14 = row[1]
                Alitude14 = float(A14)

            if row[2] == "85.5":
                B1 = row[2]
                Azimuth1 = float(B1)
            elif row[2] == "93":
                B2 = row[2]
                Azimuth2 = float(B2)
            elif row[2] == "100.7":
                B3 = row[2]
                Azimuth3 = float(B3)
            elif row[2] == "109.7":
                B4 = row[2]
                Azimuth4 = float(B4)
            elif row[2] == "121.2":
                B5 = row[2]
                Azimuth5 = float(B5)
            elif row[2] == "137.4":
                B6 = row[2]
                Azimuth6 = float(B6)
            elif row[2] == "161":
                B7 = row[2]
                Azimuth7 = float(B7)
            elif row[2] == "190.1":
                B2 = row[2]
                Azimuth8 = float(B2)
            elif row[2] == "216.1":
                B9 = row[2]
                Azimuth9 = float(B9)
            elif row[2] == "234.4":
                B10 = row[2]
                Azimuth10 = float(B10)
            elif row[2] == "247.1":
                B11 = row[2]
                Azimuth11 = float(B11)
            elif row[2] == "256.7":
                B12 = row[2]
                Azimuth12 = float(B12)
            elif row[2] == "264.8":
                B13 = row[2]
                Azimuth13 = float(B13)
            elif row[2] == "272.3":
                B14 = row[2]
                Azimuth14 = float(B14)

    #http://desktop.arcgis.com/en/arcmap/10.3/tools/spatial-analyst-toolbox/hillshade.htm

    arcpy.env.workspace = "C:\Users\patri\Desktop\Geoprogramming\Lab10_RasterOps"

    arcpy.env.overwriteOutput= True

    arcpy.CheckOutExtension("Spatial")

    Input_Raster = "smdem"


    #These values did not work because the altitude was negative.
    """Hillshade1 = Hillshade(Input_Raster,Azimuth1,Alitude1,"SHADOWS")
    Hillshade14 = Hillshade(Input_Raster,Azimuth14,Alitude14,"SHADOWS")"""

    Hillshade2 = Hillshade(Input_Raster,Azimuth2,Alitude2,"SHADOWS")
    Hillshade3 = Hillshade(Input_Raster,Azimuth3,Alitude3,"SHADOWS")
    Hillshade4 = Hillshade(Input_Raster,Azimuth4,Alitude4,"SHADOWS")
    Hillshade5 = Hillshade(Input_Raster,Azimuth5,Alitude5,"SHADOWS")
    Hillshade6 = Hillshade(Input_Raster,Azimuth6,Alitude6,"SHADOWS")
    Hillshade7 = Hillshade(Input_Raster,Azimuth7,Alitude7,"SHADOWS")
    Hillshade8 = Hillshade(Input_Raster,Azimuth8,Alitude8,"SHADOWS")
    Hillshade9 = Hillshade(Input_Raster,Azimuth9,Alitude9,"SHADOWS")
    Hillshade10 = Hillshade(Input_Raster,Azimuth10,Alitude10,"SHADOWS")
    Hillshade11 = Hillshade(Input_Raster,Azimuth11,Alitude11,"SHADOWS")
    Hillshade12 = Hillshade(Input_Raster,Azimuth12,Alitude12,"SHADOWS")
    Hillshade13 = Hillshade(Input_Raster,Azimuth13,Alitude13,"SHADOWS")

    MEGA_Hillshade_List = [

    Hillshade2,Hillshade3,Hillshade4,Hillshade5,Hillshade6,Hillshade7,
    Hillshade8, Hillshade9, Hillshade10, Hillshade11, Hillshade12, Hillshade13
    ]

    MEGA_Hillshade_sum = sum(MEGA_Hillshade_List)

    MEGA_Daylight_hours = len(MEGA_Hillshade_List)

    Average_Solar_Radiation_Hillshade = MEGA_Hillshade_sum/MEGA_Daylight_hours

    Average_Solar_Radiation_Hillshade.save()

    File.close()

if __name__ == '__main__':
    main()
