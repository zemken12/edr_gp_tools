# I played around with this idea and the way I can see someone doing it is getting a list of MXD file paths, 
# creating Map Document objects, and then appending those objects to a list based on whether Data Drive Pages are enabled.
# Depending on what you plan on doing next, you may want to pull the file paths or MXD titles, 
# and create a new list that are just unicode objects instead of MXDs. Hope this helps!
 

import arcpy
arcpy.env.workspace = r"C:\Users\zemke\Desktop\EDR\mxd_test"
list = arcpy.ListFiles("*.mxd")
 
mxdnames = []
for item in list:
    print (str(item))
    mxdnames.append(str(item))
 
mxds = []
for file in mxdnames:
    mxd = arcpy.mapping.MapDocument(r"{}\{}".format(arcpy.env.workspace,file))
    mxds.append(mxd)
 
falselist = []
for m in mxds:
    print (type(m))
    if m.isDDPEnabled == False:    
    falselist.append(m)
 
for map in falselist:
    print (map.filePath)
