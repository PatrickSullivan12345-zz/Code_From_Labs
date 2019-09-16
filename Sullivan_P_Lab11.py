#-------------------------------------------------------------------------------
# Name:        Patrick Sullivan
# Purpose:     Lab11
#
# Author:      pps7
#
# Created:     03/04/2018
# Copyright:   (c) pps7 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

    """This script will take the user input and turn the selected layer on and
    all the other layers off."""

    import arcpy

    User_Input = arcpy.GetParameterAsText(0)
    Lyr_On = str(User_Input)

    mxd = arcpy.mapping.MapDocument("CURRENT")
    df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
    All_Lyrs = arcpy.mapping.ListLayers( mxd, "*", df )

    for lyr in All_Lyrs:
        if lyr.name == Lyr_On:
            lyr.visible = True
        else:
            lyr.visible = False

if __name__ == '__main__':
    main()
