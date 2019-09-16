#-------------------------------------------------------------------------------
# Name:        Lab 5
# Purpose:
#
# Author:      Patrick O'Sullivan
#
# Created:     15/02/2018
# Copyright:   (c) pps7 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

    #Question 1
    #Turn on the visibility of layer that matches user input of a layer name but
    #turn off all other layers

def Turn_Layers_On():

    import arcpy

    #I was confused on how to write the input for ArcMap, so I left this here
    #for reference

    #User_Layer = arcpy.AddMessage('Please enter a Layer you want to turn on:' )
    #User_Input = arcpy.GetParameterAsText(0)
    #C:\Users\patri\Desktop\Geoprogramming\Lab 5\Lab5.mxd

    User_Input = raw_input("Please enter the layer you want to turn on")
    Lyr_On = str(User_Input)

    mxd = arcpy.mapping.MapDocument("CURRENT")
    df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
    All_Lyrs = arcpy.mapping.ListLayers( mxd, "*", df )

    for lyr in All_Lyrs:
        if lyr.name == Lyr_On:
            lyr.visible = True
        else:
            lyr.visible = False

    mxd.save()

def Change_Transparency():

    #Question 2
    #Set the transparency of all feature layers to 30% and raster layers to 60%

    import arcpy

    mxd = arcpy.mapping.MapDocument("CURRENT")
    df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
    All_Lyrs = arcpy.mapping.ListLayers( mxd, "*", df )

    for lyr in All_Lyrs:
        if lyr.isFeatureLayer:
            lyr.transparency = 30

        elif lyr.isRasterLayer:
            lyr.transparency = 60

    mxd.save()

if __name__ == '__main__':
    main()
    Turn_Layers_On()
    Change_Transparency()

