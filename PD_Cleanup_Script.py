# Author Brad Stephenson
# worked with Joe and Michael 

import arcpy


# path to the dbf containing the data - change this to run on another machine
dbf = "C:\\Users\\Brad\\Documents\\ArcGIS\\Export_PD_Fixed.dbf"

try:
    arcpy.DeleteField_management(dbf, "Address")
except:
    pass

try:
    arcpy.AddField_management(dbf, "Address", "String", 100)
except:
    arcpy.AddMessage("Could not add Address.")

try:
    arcpy.DeleteField_management(dbf, "Apt")
except:
    pass

try:
    arcpy.AddField_management(dbf, "Apt", "String", 10)
except:
    arcpy.AddMessage("Could not add Address.")

# setup two cursors, a search and an update       
search = arcpy.da.SearchCursor(dbf, ("Dir", "Num", "Street", "Address"))
update = arcpy.da.UpdateCursor(dbf, ("Address", "Apt"))

# Setup variable to hold street name so that lower rows can use
# value from rows above
LastKnownStreetName = ""
FullStreet = ""

# apptNum is a string that represents the apptnum
apptNum = ""

# Locality will be a direction, N, E, S, W
localityLetter = "z"


# This flag will be false when locality has something else in it
localityDescribesDirection = False

# This will contain all the completed addresses for the update cursor to use
addresses = []
appts = []


for row in search:
    # always reset flags at the beggining of a loop
    localityDescribesDirection = False
    # blank cells have " " in them
    if row[2] != " ":
        # store street name for lower rows to use if they don't have thier own
        LastKnownStreetName = row[2]
        
            
        # sometimes direction is stored in street name
        if LastKnownStreetName[1] == " ":
            # grab the letter and sotre in localityLetter
            localityLetter = LastKnownStreetName[0]
            # remove locality from street name
            LastKnownStreetName = LastKnownStreetName[2:]
    index = LastKnownStreetName.find("#")
    if index != -1:
        apptNum = LastKnownStreetName[index + 1:]
        while apptNum[0] == " ":
            apptNum = apptNum[1:]
        while apptNum[-1] == " ":
            apptNum = apptNum[:-1]
    else:
        apptNum = ""
    appts.append(apptNum)
    # note: locality letter is not reset at the top or bottom of a loop, so
    # when it is taken from the street name, it is persistent. It does not need
    # to be taken multiple times, which is why it is safe to remove the letter
    # from the also persistant LastKnownStreetName variable

    # Special Case
    if row[0] == "EWUMAIN":
        localityLetter = "N"
        LastKnownStreetName = "170TH"


    # Find locality Letter 
    if row[0].upper() == "NORTH":
        localityLetter = "N"
        localityDescribesDirection = True
    if row[0].upper() == "SOUTH":
        localityLetter = "S"
        localityDescribesDirection = True
    if row[0].upper() == "EAST":
        localityLetter = "E"
        localityDescribesDirection = True 
    if row[0].upper() == "WEST":
        localityLetter = "W"
        localityDescribesDirection = True
    if row[0].upper() == "EWUMAIN":
        localityLetter = "N"
    

    # If locality describes direction, use it as LocalityLetter
    if localityDescribesDirection == True:
        localityLetter = row[0][0]


    # Build street
    FullStreet = localityLetter + " " + LastKnownStreetName
    #build complete address
    CompleteAddress = "" + str(   int(row[1])    ) + " " + FullStreet

    # Special CAse
    if row[0] == "NELM":
        CompleteAddress = "Could not calculate address"

    print CompleteAddress

    # put complete address in list
    addresses.append(CompleteAddress)

i = 0
#del row
#del search

# use list to populate address field in fixed dbf
for row in update:
    print addresses[i], appts[i]
    row[0] = addresses[i]
    row[1] = appts[i]
    update.updateRow(row)
    i += 1
    

