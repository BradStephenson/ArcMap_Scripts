import arcpy
# grab a reference to the current document
mxd = arcpy.mapping.MapDocument("C:/Users/Brad/Documents/ArcGIS/PythonActivityDay4.mxd")

# get a list of all the layers in the given document
layerList = arcpy.mapping.ListLayers(mxd)
for lyr in layerList:
    print lyr.name

# get a list of all the fields in the first layer in the list of layers
pumpFields = arcpy.ListFields(layerList[0].dataSource)

# print some info on the fields
for field in pumpFields:
    print field.name, ": ", field.type, ", ", field.length

layerName = layerList[0].dataSource
fieldName = pumpFields[3].name



# search through the shape vertices in the first layer, print info about them
for row in arcpy.da.SearchCursor(layerName, ["SHAPE@XY"]):
    x, y = row[0]
    print( "{0},{1}".format(x, y))

# insert a single line
with arcpy.da.InsertCursor(layerList[2].dataSource, ("SHAPE@XY", "NAME")) as cursor:
    cursor.insertRow(((float(-81.8), float(24.55)), "Newer Airport"))

# change fields in a layer
with arcpy.da.UpdateCursor(layerList[2].dataSource, ("NAME")) as cursor:
    for row in cursor:
        row[0] = "Better Name"
        cursor.updateRow(row)

# more dynamic changes
with arcpy.da.UpdateCursor(layerList[2].dataSource, ("NAME", "STATE")) as cursor:
    for row in cursor:
        if row[1] == "Florida":
            row[0] = "Another Airport"
            cursor.updateRow(row)
