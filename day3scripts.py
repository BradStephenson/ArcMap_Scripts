# Author Bradley Stephenson
# This is to be run with a map that has broken links for layer data sources

# Get  a reference to the doc
mxd = arcpy.mapping.MapDocument("CURRENT")
# grab the list of layers in the map
layerList = arcpy.mapping.ListLayers(mxd)



# start at 0 
num = 0
# count the number of broken links
for lyr in layerList:
    if lyr.isBroken:
        num += 1
        
# report the total    
print num
