# Author Bradley Stephenson

import arcpy
import math

def main():
    # Get the names of shapefiles from the user
    statesFile = arcpy.GetParameterAsText(0)[0:-3] + "dbf"
    districtsFile = arcpy.GetParameterAsText(1)[0:-3] + "dbf"
    # Taking the names of .shp but using them as .dbf - only taking as shp because the shpaefile is sort of the main
    # file and the dbf is sort of a supporting file. 


    # These will be added a fields and used for storing the area and length of the states/districts
    areaName = "pp_area"

    perimeterName = "pp_peri"

    
    # default names used while I tested - these are the names for most shapefiles online that work for this program
    statesFileName = "NAME"
    districtsFileName = "XmlToTbl_s"

    # allow the user to specify a name for the states in both files.
    statesFileName = arcpy.GetParameterAsText(2)
    districtsFileName = arcpy.GetParameterAsText(3)
    

    # geoprocessing to fill the area and length fields in the files
    addAreaPerimeter(statesFile, areaName, perimeterName)

    addAreaPerimeter(districtsFile, areaName, perimeterName)

    

    # Very carefully make sure we have exactly the right fields

    try:
        arcpy.DeleteField_management(statesFile, "wCompact")
    except:
        pass

    try:
        arcpy.DeleteField_management(statesFile, "statePolPo")
    except:
        pass

    try:
        arcpy.DeleteField_management(statesFile, "avDistrict")
    except:
        pass

    try:
        arcpy.AddField_management(statesFile, "wCompact", "FLOAT", 6)
    except:
        arcpy.AddMessage("Could not add wCompact.")

    try:
        arcpy.AddField_management(statesFile, "statePolPo", "FLOAT", 6)
    except:
        arcpy.AddMessage("Could not add statePolPo.")

    try:
        arcpy.AddField_management(statesFile, "avDistrict", "FLOAT", 6)
    except:
        arcpy.AddMessage("Could not add avDistrict.")

        
    # setup searches
    stateSearch = arcpy.da.SearchCursor(statesFile,(areaName, perimeterName, statesFileName))
    districtsSearch = arcpy.da.SearchCursor(districtsFile,(areaName, perimeterName, districtsFileName))
    # get ready to pudate states file with the data we want
    stateUpdate = arcpy.da.UpdateCursor(statesFile,("statePolPo", "avDistrict", "wCompact"))

    # make an empty list of states
    states = []

    # fill the states list with instances of state, by grabbing data from the dbfs
    for row in stateSearch:
        states.append(State(row[2], row[0], row[1]))

    for row in districtsSearch:
        addCountyPolPop(row[2], polsbypopper(row[0], row[1]), states)

    # for each state, calc the average compactness of the districts in the state
    for state in states:
        state.calcAverage()

    # update the states file with the compactness data
    index = 0
    for row in stateUpdate:
        row[0] = states[index].getStatePolPop()
        row[1] = states[index].getAvCountyPolPop()
        row[2] = states[index].getWeightedCompactness()
        stateUpdate.updateRow(row)
        index += 1

    del row
    del stateSearch
    del districtsSearch
    del stateUpdate

    # add the states file as a layer to the current document 
    try:
        addShapefileAsLayer(statesFile[0:-3])
    except:
        arcpy.AddMessage("Could not add layer.")
        print "Could not add layer."

    arcpy.AddMessage("Finished. You should see a layer containing the results of the analysis on your map.")
    arcpy.AddMessage("avDistrictPo is a measure of the average compactness of the districts in the state")
    arcpy.AddMessage("wCompact is the average compactness weighted by the compactness of the state")


def addShapefileAsLayer(filePathWithoutExt):
    # This function adds the shapefile specified to the current mxd. It does not change symbology - which is
    # not possible to do programmatically without having a layer already with the desired symbology.
    mxd = arcpy.mapping.MapDocument("CURRENT")

    df = arcpy.mapping.ListDataFrames(mxd,"*")[0]

    newlayer = arcpy.mapping.Layer(filePathWithoutExt + "shp")

    arcpy.mapping.AddLayer(df, newlayer,"TOP")

    

def addAreaPerimeter(dbfPath, areaName, perimeterName):
    # This function adds fields to the specified dbf and calculates area and
    # perimeter for each row based on the shapfile accompanying the dbf
    
    # first make sure we have the fields we want
    try:
        arcpy.DeleteField_management(dbfPath, areaName)
        arcpy.DeleteField_management(dbfPath, perimeterName)
    except:
        print "one or more fields not found. Creating..."

    try:
        arcpy.AddField_management(dbfPath, areaName, "FLOAT", 6)
        arcpy.AddField_management(dbfPath, perimeterName, "FLOAT", 6)
    except:
        print "WARNING!   was not able to add pp_area or pp_perimeter fields"

    # this is the geometries from the .shp that comes with the dbf
    geometries = arcpy.CopyFeatures_management(dbfPath[0:-3] + "shp", arcpy.Geometry())

    # setup lists
    areas = []
    perimeters = []

    # fill lists with data from geometries
    for geometry in geometries:
        areas.append(geometry.getArea("GEODESIC"))
        perimeters.append(geometry.getLength("GEODESIC"))
        print "Area:", geometry.getArea("GEODESIC"), "Length:", geometry.getLength("GEODESIC")

    # put the data from the geometries into the dbf in the new fields we just made
    i = 0
    updateCursor = arcpy.da.UpdateCursor(dbfPath,(areaName, perimeterName))

    for row in updateCursor:
        row[0] = areas[i]
        row[1] = perimeters[i]
        updateCursor.updateRow(row)
        i += 1

    # clear references
    del row
    del updateCursor
    del geometries

    
def getStateByName(stateName, states):
    # returns the state onject associated with the given state name - O(n) is ok here because there will not be many
    # more than 50 state objects
    for state in states:
        if state.getName() == stateName:
            return state

def addCountyPolPop(stateName, polPop, states):
    # adds infor for a single district to a state object,
    # which will keep track of them all and do calculation based on them
    for state in states:
        if state.getName() == stateName:
            state.addCountyPolPop(polPop)
            print stateName, polPop
            return


def polsbypopper(area, perimeter):
    # This is the math that is the Polsby-Popper method of determining compactness
    try:
        return (4 * math.pi * area)/(perimeter*perimeter)
    except:
        return 1
    
class State:
    # This is a class that I use only in the python context to temporarily store information about states

    def __init__(self, name, area, perimeter):
        self.name = name
        self.statePolPop = polsbypopper(area, perimeter)
        self.tonedDownPolPop = self.statePolPop +( (1.0 - self.statePolPop) / 2.0)
        self.avCountyPolPop = 0.0
        self.countyPolPops = []
        self.weightedCompactness = 0.0

    def getName(self):
        return self.name
    def getStatePolPop(self):
        return self.statePolPop
    
    def getAvCountyPolPop(self):
        return self.avCountyPolPop

    def getWeightedCompactness(self):
        return self.weightedCompactness

    def addCountyPolPop(self, polPop):
        self.countyPolPops.append(polPop)

    # This method has the state calculate average compactness of the districts in the state
    # it updates the weightedcompactness and the avCountyPolPop fields only in the context of the state class
    # these values must be updated to the dbf separately.
    def calcAverage(self):
        self.avCountyPolPop = 0.0
        print "-----", self.name, "----"
        for polPop in self.countyPolPops:
            self.avCountyPolPop += polPop
            print polPop
        try:
            self.avCountyPolPop /= len(self.countyPolPops)
        except:
            self.avCountyPolPop = 1

        self.weightedCompactness = self.avCountyPolPop/ self.tonedDownPolPop
        
    # not currently used
    def getMultiplier(self):
        return 1
    






main()
