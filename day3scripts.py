mxd = arcpy.mapping.MapDocument("CURRENT")
layerList = arcpy.mapping.ListLayers(mxd)
for lyr in layerList:
    print lyr.name
    
descriptions = []
for lyr in layerList:
    descriptions.append(arcpy.Describe(lyr))
    
arcpy.Describe("elev")
for lyr in layerList:
    descriptions.append(arcpy.Describe(lyr.name))
    
for lyr in layerList:
    try:
        descriptions.append(arcpy.Describe(lyr.name))
    except RuntimeError:
        
for lyr in layerList:
    try:
        descriptions.append(arcpy.Describe(lyr.name))
    except RuntimeError:
        
brokenLinkNum = 0
for lyr in layerList:
    try:
        descriptions.append(arcpy.Describe(lyr.name))
    except RuntimeError:
        brokenLinkNum += 1
        
for lyr in layerList:
    try:
        descriptions.append(arcpy.Describe(lyr.name))
    except Exception:
        brokenLinkNum += 1
        

print brokenLinkNum
arcpy.Describe("Rivers")
print arcpy.Describe("elev")
desc =  arcpy.Describe("elev")
fields = desc.fields
for f in fields:
    print f
    
for f in fields:
    print f.name
    
ly = layerList[5]
print ly
ly.dataSource
layerList[0].dataSource
ly.isBroken
for lyr in layerList:
    if lyr.isBroken:
        num++
        
num = 0
for lyr in layerList:
    if lyr.isBroken:
        num += 1
        
print num
def showVectorHideRaster():
    mxd = arcpy.mapping.MapDocument("CURRENT")
    layerList = arcpy.mapping.listLayers(mxd)
    for lyr in layerList:
        if lyr.isFeatureLayer:
            lyr.visible = true
        else:
            lyr.visible = false
            
showVectorHideRaster()
def showVectorHideRaster():
    mxd = arcpy.mapping.MapDocument("CURRENT")
    layerList = arcpy.mapping.ListLayers(mxd)
    for lyr in layerList:
        if lyr.isFeatureLayer:
            lyr.visible = true
        else:
            lyr.visible = false
            
showVectorHideRaster()
def showVectorHideRaster():
    mxd = arcpy.mapping.MapDocument("CURRENT")
    layerList = arcpy.mapping.ListLayers(mxd)
    for lyr in layerList:
        if lyr.isFeatureLayer:
            lyr.visible = True
        else:
            lyr.visible = False
            
showVectorHideRaster()
showVectorHideRaster()
showVectorHideRaster()
def allInvisible():
    mxd = arcpy.mapping.MapDocument("CURRENT")
    layerList = arcpy.mapping.ListLayers(mxd)
    for lyr in layerList:
        print lyr.name
        
allInvisible()
def allInvisible():
    mxd = arcpy.mapping.MapDocument("CURRENT")
    layerList = arcpy.mapping.ListLayers(mxd)
    for lyr in layerList:
        lyr.visible = False
        
allInvisible()
def allInvisible():
    mxd = arcpy.mapping.MapDocument("CURRENT")
    layerList = arcpy.mapping.ListLayers(mxd)
    for lyr in layerList:
        lyr.visible = false
        
allInvisible()
def allInvisible():
    mxd = arcpy.mapping.MapDocument("CURRENT")
    layerList = arcpy.mapping.ListLayers(mxd)
    for i in range (0,layerList.count):
        layerList[i].visible = False
        
allInvisible()
def allInvisible():
    mxd = arcpy.mapping.MapDocument("CURRENT")
    layerList = arcpy.mapping.ListLayers(mxd)
    for i in range (0,12):
        layerList[i].visible = False
        
allInvisible()
def allVisible():
    mxd = arcpy.mapping.MapDocument("CURRENT")
    layerList = arcpy.mapping.ListLayers(mxd)
    for i in range (0,12):
        layerList[i].visible = True
        
allVisible()
def allVisible():
    mxd = arcpy.mapping.MapDocument("CURRENT")
    layerList = arcpy.mapping.ListLayers(mxd)
    for i in range (0,12):
        layerList[i].visible = True
    arcpy.RefreshActiveView()
    arcpy.RefreshCatalog()
    
def allInvisible():
    mxd = arcpy.mapping.MapDocument("CURRENT")
    layerList = arcpy.mapping.ListLayers(mxd)
    for i in range (0,12):
        layerList[i].visible = False
    arcpy.RefreshActiveView()
    arcpy.RefreshCatalog()
    
allInvisible()
def allInvisible():
    mxd = arcpy.mapping.MapDocument("CURRENT")
    layerList = arcpy.mapping.ListLayers(mxd)
    for i in range (0,12):
        layerList[i].visible = False
    arcpy.RefreshActiveView()
    
def allVisible():
    mxd = arcpy.mapping.MapDocument("CURRENT")
    layerList = arcpy.mapping.ListLayers(mxd)
    for i in range (0,12):
        layerList[i].visible = True
    arcpy.RefreshActiveView()
    
allVisible()
def allInvisible():
    mxd = arcpy.mapping.MapDocument("CURRENT")
    layerList = arcpy.mapping.ListLayers(mxd)
    for lyr in layerList):
        lyr.visible = False
    arcpy.RefreshActiveView()
    
def allInvisible():
    mxd = arcpy.mapping.MapDocument("CURRENT")
    layerList = arcpy.mapping.ListLayers(mxd)
    for lyr in layerList:
        lyr.visible = False
    arcpy.RefreshActiveView()
    
allInvisible()
def allVisible():
    mxd = arcpy.mapping.MapDocument("CURRENT")
    layerList = arcpy.mapping.ListLayers(mxd)
    for lyr in layerList:
        lyr.visible = True
    arcpy.RefreshActiveView()
    
def showVectorHideRaster():
    mxd = arcpy.mapping.MapDocument("CURRENT")
    layerList = arcpy.mapping.listLayers(mxd)
    for lyr in layerList:
        if lyr.isFeatureLayer:
            lyr.visible = True
        else:
            lyr.visible = False
    arcpy.RefreshActiveView()
    
showVectorHideRaster()
def showVectorHideRaster():
    mxd = arcpy.mapping.MapDocument("CURRENT")
    layerList = arcpy.mapping.ListLayers(mxd)
    for lyr in layerList:
        if lyr.isFeatureLayer:
            lyr.visible = True
        else:
            lyr.visible = False
    arcpy.RefreshActiveView()
    
showVectorHideRaster()

