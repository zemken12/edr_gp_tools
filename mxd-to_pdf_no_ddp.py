#Script takes all .mxd files in a user defined directory and
#exports them to the user defined directory

#imports relevant modules
import os, arcpy

#user sets input and output directories
input_dir = arcpy.GetParameterAsText(0)
output_dir = arcpy.GetParameterAsText(1)

arcpy.env.workspace = ws = str(input_dir)

mxd_list = arcpy.ListFiles("*.mxd")

for mxd in mxd_list:
    #creates variable that opens an arcmap document at input dir + .mxd
    current_mxd = arcpy.mapping.MapDocument(os.path.join(ws, mxd))
    #creates variable that stores output directory + mxd
    pdf_name = (os.path.join(output_dir, mxd[:-4]) + ".pdf")
    #exports the mxd to the output folder
    arcpy.mapping.ExportToPDF(current_mxd, pdf_name)
    arcpy.AddMessage('\t' + mxd + str(' exported successfully.'))
del mxd_list

arcpy.AddMessage(('Exports complete!'))

complete = os.startfile(output_dir)
complete


