#-------------------------------------------------------------------------------
# Name:        Patrick O'Sullivan
# Purpose:     Lab 7
#
# Author:      Patrick
#
# Created:     10/03/2018
# Copyright:   (c) patri 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

def Lab7(list_groups):

    import arcpy
    arcpy.env.workspace = "C:\Users\patri\Desktop\Geoprogramming\Lab7"

    arcpy.MakeFeatureLayer_management("HaysBG00.shp", "HaysBG00Lyr" )
    arcpy.MakeFeatureLayer_management("Hays_rivers.shp", "RiverLyr")

    totalpop = 0
    totallength = 0

    with open("Lab7.txt", "a+") as tf:
        tf.write("Block_ID, Block_Count, Block_TotalPop, River_Length\n")
        with arcpy.da.SearchCursor("HaysBG00Lyr", ["GROUP"]) as cursor:
            for row in cursor:
                list_groups.append(row[0])
        list_groups = list(set(list_groups))

        Path = "C:\Users\patri\Desktop\Geoprogramming\Lab7\HaysBG00.shp"
        Fields = ["MALES" , "FEMALES","POP2000"]
        with arcpy.da.UpdateCursor(Path, Fields) as cursor:
            for row in cursor:
                row[2] = row[0] + row[1]
                totalpop += row[2]

        Field = ["Length"]
        arcpy.SelectLayerByLocation_management("HaysBG00Lyr","INTERSECT", "RiverLyr")
        sName = "River_Intersection.shp"
        #arcpy.CopyFeatures_management("RiverLyr", sName)
        Path2 = "C:\Users\patri\Desktop\Geoprogramming\Lab7\River_Intersection.shp"
        with arcpy.da.UpdateCursor(Path2, Field) as cursor:
            for row2 in cursor:
                totallength += row2[0]

        for block_id in list_groups:
            str_sql = """ "WHITE" > 500 and "GROUP" = ' {0} ' """.format(block_id)
            arcpy.SelectLayerByAttribute_management("HaysBG00Lyr","NEW_SELECTION",str_sql)
            tf.write(block_id + "\n")

        tf.write("         " + str(block_id) +" counts, " + str(totalpop) + " people, " + str(totallength) + " meters\n")


if __name__ == '__main__':
    main()
    Lab7(["GROUP"])
