def showVectorHideRaster():
    mxd = arcpy.mapping.MapDocument("CURRENT")
    layerList = arcpy.mapping.ListLayers(mxd)
    for lyr in layerList:
        if lyr.isFeatureLayer:
            lyr.visible = True
        else:
            lyr.visible = False
    arcpy.RefreshActiveView()

def allVisible():
    mxd = arcpy.mapping.MapDocument("CURRENT")
    layerList = arcpy.mapping.ListLayers(mxd)
    for lyr in layerList:
        lyr.visible = True
    arcpy.RefreshActiveView()

def allInvisible():
    mxd = arcpy.mapping.MapDocument("CURRENT")
    layerList = arcpy.mapping.ListLayers(mxd)
    for lyr in layerList:
        lyr.visible = False
    arcpy.RefreshActiveView()




