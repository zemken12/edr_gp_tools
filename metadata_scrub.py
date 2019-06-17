# Metadata editor
# Edit existing metadata fields. Specifically the summary, and description
import arcpy
import arcpy_metadata as md

# have the user point to a directory that contains all shps/xmls? that need to be scrubbed

dir = arcpy.GetParameterAsText(0) # location of VSR Polygons
arcpy.env.workspace = ws = dir
# create a list of shapefiles? or xmls?

scrub_list = arcpy.ListData("*.xml")

# edit existing metadata for shps, rasters, fc, rd, md
metadata = md.MetadataEditor(scrub_list)  #supports shp, fc, RasterDatasets and Layers

# edit/create XML file directly
metadata = md.MetadataEditor(metadata_file="path/to/metadata_file.xml")

# Get text items (returns string)
description = metadata.description
summary = metadata.summary

# Change text items
metadata.title = "The new title"
metadata.purpose = "This is the abstract"
metadata.summary = ""
metadata.purpose = ""

metadata.finish()  # save() and cleanup() as one call
