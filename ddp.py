import arcpy
arcpy.env.workspace = r"C:\Users\username\Desktop"
list = arcpy.ListFiles("*.mxd")
 
mxdnames = []
for item in list:
... print (str(item))
... mxdnames.append(str(item))
 
mxds = []
for file in mxdnames:
... mxd = arcpy.mapping.MapDocument(r"{}\{}".format(arcpy.env.workspace,file))
... mxds.append(mxd)
 
falselist = []
for m in mxds:
... print (type(m))
... if m.isDDPEnabled == False:
...    falselist.append(m)
 
for map in falselist:
... print (map.filePath)
