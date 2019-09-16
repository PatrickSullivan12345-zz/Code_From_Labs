#-------------------------------------------------------------------------------
# Name:        Patrick O'Sullivan
# Purpose:     Lab 6
#
# Author:      Patrick
#
# Created:     23/02/2018
# Copyright:   (c) patri 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

def Question_1():
    """Psuedocode for question 2.1:
    1. Follow the link here for create feature class, make sure you include the
    parameters correctly.
    http://pro.arcgis.com/en/pro-app/tool-reference/data-management/create-feature-class.htm

    2.Second step is to create a list of point array. take a look at the
    following example for two polylines, line = ([[100,200],[300,400]],
    [[500,600],[700,800]])

    3.Then you use the cur=da.InsertCursor(......) to insert the polyline

    4.Then you use the cur.insertRow()
    at the end make sure you delete the cursor"""

    import arcpy

    path = ("C:\Users\patri\Desktop\Geoprogramming\Lab6\Lab6a_FeatureClass")

    arcpy.env.workspace = ("C:\Users\patri\Desktop\Geoprogramming\Lab6\Lab6a_FeatureClass")
    arcpy.env.overwriteOutput= True

    Spatial_Reference = arcpy.Describe("C:\Users\patri\Desktop\Geoprogramming\Lab6\Lab6a_FeatureClass\Schools.shp").SpatialReference

    arcpy.CreateFeatureclass_management(path,"Schools_Poly.shp","POLYLINE","","","",Spatial_Reference)

    Poly = ([[100,100],[100,400]],[[200,100],[200,200]])

    cur = arcpy.da.InsertCursor("Schools_Poly.shp",["SHAPE@"])

    for xy in Poly:
        cur.insertRow([xy])
    #cur.insertRow([Poly])

    del cur

def Question_2():
    """
    Psuedocode for question 2.2:
    1. Import system modules

    2. Create random points in the features of a constraining feature class
    Number of points for each feature determined by the value in the field
    specified

    3. Set workspace

    4. Create fields for random values

    5. Calculate random values between 1-100 in the new fields
    """
    import arcpy

    out_path = ("C:\Users\pps7\Desktop\Lab6\Lab6a_FeatureClass")

    arcpy.env.workspace = ("C:\Users\pps7\Desktop\Lab6\Lab6a_FeatureClass")
    arcpy.env.overwriteOutput= True

    #Spatial_Reference = arcpy.Describe("C:\Users\pps7\Desktop\Lab6\Lab6a_FeatureClass\Schools").SpatialReference

    Output_Name = "School_Random_pts"
    Concise_FC = "C:\Users\pps7\Desktop\Lab6\Lab6a_FeatureClass\Schools.shp"
    Number_of_Points = 100
    arcpy.CreateRandomPoints_management(out_path,Output_Name,Concise_FC,"",100)

def Question_3():

    import arcpy
    from arcpy import env
    from arcpy.sa import *

    arcpy.env.workspace = "C:\Users\patri\Desktop\Geoprogramming\Lab6\Lab6b_Raster"
    arcpy.env.overwriteOutput= True

    Input_Raster = "dem"
    az = 260
    alt = 60
    Shadows = "SHADOWS"
    zF = 0.348

    arcpy.CheckOutExtension("Spatial")


    Aspect = Aspect(Input_Raster,"PLANAR","MILE_US")
    Aspect.save("Aspect")
    AspectPath = "C:\Users\patri\Desktop\Geoprogramming\Lab6\Lab6b_Raster\Aspect"

    Hillshade = Hillshade(Input_Raster,az,alt,Shadows,zF)
    Hillshade.save("Hillshade")
    HillshadePath ="C:\Users\patri\Desktop\Geoprogramming\Lab6\Lab6b_Raster\Hillshade"

    Sum = Raster(AspectPath) + Raster(HillshadePath)
    Sum.save("Sum")

    """You can use the arcpy cursor function to access an Excel spread sheet. True or False?
    True"""


if __name__ == '__main__':
    main()
    Question_1()
    #Question_2()
    #Question_3()