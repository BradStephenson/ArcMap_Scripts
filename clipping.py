import arcpy
# clip a set of rasters with a polygon

folder = arcpy.GetParameterAsText(0)

arcpy.env.workspace = folder

input_poly_name = arcpy.GetParameterAsText(1)


#rasters = arcpy.da.Walk(folder, datatype="RasterDatasetr")
rasters = arcpy.ListRasters()

letter = 'a'


for r in rasters:
    newName = r[0:-4] + "_clip_" + r[-4:]
    arcpy.Clip_management(r, "#", newName, input_poly_name, "0", "ClippingGeometry")


#arcpy.Clip_management("c:\\test\\image.tif", "0 0 0 0", 
  #                    "c:\\output\\clip.tif", input_poly_name, "0", "ClippingGeometry")








