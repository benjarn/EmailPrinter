# Printer example cups simple
import cups

# print the file using cups
conn = cups.Connection()
# Get a list of all printers
printers = conn.getPrinters()
for printer in printers: 
# Print name of printers to stdout (screen)
    print printer, printers[printer]["device-uri"]
# get first printer from printer list
printer_name = printers.keys()[0]
conn.printFile(printer_name, filename,
"Python_Status_print", {})
