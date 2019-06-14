import arcpy
mxd = arcpy.mapping.MapDocument("C:/Users/Brad/Documents/ArcGIS/PythonActivityDay4.mxd")


layerList = arcpy.mapping.ListLayers(mxd)
for lyr in layerList:
    print lyr.name

    
pumpFields = arcpy.ListFields(layerList[0].dataSource)

for field in pumpFields:
    print field.name, ": ", field.type, ", ", field.length

layerName = layerList[0].dataSource
fieldName = pumpFields[3].name

#for row in arcpy.da.SearchCursor(layerName, fieldName):
#print row[0]


for row in arcpy.da.SearchCursor(layerName, ["SHAPE@XY"]):
    x, y = row[0]
    print( "{0},{1}".format(x, y))

with arcpy.da.InsertCursor(layerList[2].dataSource, ("SHAPE@XY", "NAME")) as cursor:
    cursor.insertRow(((float(-81.8), float(24.55)), "Newer Airport"))

with arcpy.da.UpdateCursor(layerList[2].dataSource, ("NAME")) as cursor:
    for row in cursor:
        row[0] = "Better Name"
        cursor.updateRow(row)

    
with arcpy.da.UpdateCursor(layerList[2].dataSource, ("NAME", "STATE")) as cursor:
    for row in cursor:
        if row[1] == "Florida":
            row[0] = "Another Airport"
            cursor.updateRow(row)
