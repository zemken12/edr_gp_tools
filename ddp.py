# Shelby Zemken 06/11/2019    zemken12@gmail.com
# This script prompts a user for an input directory containing MXDs,
# and prompts for an output directory where PDFs are batch exported
# This script exports both normal MXDs and MXDs with data driven pages enabled.

import os, arcpy

# user sets input and output directories
input_dir = arcpy.GetParameterAsText(0)
output_dir = arcpy.GetParameterAsText(1)
arcpy.env.workspace = ws = str(input_dir)
mxdnames = arcpy.ListFiles("*.mxd")

for documentname in mxdnames:
    input = os.path.join(ws, documentname)
    mxd = arcpy.mapping.MapDocument(input)
    output_name = (os.path.join(output_dir, documentname[:-4]) + ".pdf")
    if hasattr(mxd, "dataDrivenPages"):
        ddp = mxd.dataDrivenPages
        ddp.exportToPDF(output_name, "ALL")
        arcpy.AddMessage('\t' + str(mxd) + str(' exported successfully (Data Driven Pages Enabled).'))
        del mxd
    else:
        arcpy.mapping.ExportToPDF(mxd, output_name)
        arcpy.AddMessage('\t' + str(mxd) + str(' exported successfully.'))
        del mxd

arcpy.AddMessage(('Exports complete!'))
complete = os.startfile(output_dir)
complete

