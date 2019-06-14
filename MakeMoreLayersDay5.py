import arcpy

fc1 = "C:\\Users\\Brad\\Documents\\ArcGIS\\Day5\\counties\\wa_counties.shp"
fc2 = "C:\\Users\\Brad\\Documents\\ArcGIS\\Day5\\toxic\\toxicWA2009.shp"

arcpy.MakeFeatureLayer_management(fc1, "countylyr")
arcpy.MakeFeatureLayer_management(fc2, "toxiclyr")
arcpy.SelectLayerByAttribute_management("countylyr", "NEW_SELECTION", '"NAME10" = \'Ki\*\';DROP TABLE *;')
arcpy.CopyFeatures_management("countylyr", "C:/Users/Brad/Documents/ArcGIS/Day5/copies/ki.shp")


#arcpy.CopyFeatures
