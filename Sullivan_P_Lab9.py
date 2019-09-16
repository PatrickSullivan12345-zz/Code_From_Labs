#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      patri
#
# Created:     25/03/2018
# Copyright:   (c) patri 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

    import arcpy

    arcpy.env.workspace = "C:\Users\patri\Desktop\Geoprogramming\Lab9_Layout"

    mxd = arcpy.mapping.MapDocument("CURRENT")

    DDP = mxd.dataDrivenPages
    DDP.exportToPDF("lab9DDP.pdf")

if __name__ == '__main__':
    main()
