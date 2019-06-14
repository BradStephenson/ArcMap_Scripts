import arcpy
import os

countyName = arcpy.GetParameterAsText(0)

#folderName = arcpy.GetParameterAsText(1)

fc1 = "C:\\Users\\Brad\\Documents\\ArcGIS\\Day5\\counties\\wa_counties.shp"
fc2 = "C:\\Users\\Brad\\Documents\\ArcGIS\\Day5\\toxic\\toxicWA2009.shp"

sc = "C:/Users/Brad/Documents/ArcGIS/TempScriptFolder/selectedCounty"
scSHP = "C:/Users/Brad/Documents/ArcGIS/TempScriptFolder/selectedCounty.shp"

sqlString = '"NAME10" = \''+countyName+'\''

arcpy.MakeFeatureLayer_management(fc1, "countylyr")
arcpy.MakeFeatureLayer_management(fc2, "toxiclyr")

arcpy.SelectLayerByAttribute_management("countylyr", "NEW_SELECTION", sqlString)

arcpy.CopyFeatures_management("countylyr", sc)
arcpy.MakeFeatureLayer_management(scSHP, "selectedCounty")
arcpy.SelectLayerByLocation_management("toxiclyr", "COMPLETELY_WITHIN","selectedCounty")

"""files = os.listdir("C:/Users/Brad/Documents/ArcGIS/TempScriptFolder/")

fi = files[0]

fi.

for f in files:
    os.remove("C:/Users/Brad/Documents/ArcGIS/TempScriptFolder/"+f)
"""
arcpy.CopyFeatures_management("toxiclyr", "C:/Users/Brad/Documents/ArcGIS/TempScriptFolder/toxinsInCounty")

arcpy.AddMessage("Done.")

