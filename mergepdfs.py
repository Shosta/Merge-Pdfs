'''
Hello
'''
#!/usr/bin/python3

import os.path
import string
import parsepdfsfile


# import sys
# sys.argv[1] le premier argument de la commande lorsque l'on lance la commande depuis un terminal.

#PATH = "C:\\Remi\\Developpement\\A traiter"
PATH = "/Users/Shosta/Developpement/A traiter"
# PATH = 'C:\\Remi\\ShostaSync\\Scans a traiter'

def merge_pdf_files(file_names_list):
	# Create a PdfFileMerger object.
    from PyPDF2 import PdfFileMerger, PdfFileReader
    first_file_index = 0
    counter = 1

    # Go through all elements of the list.
    for first_file_index in range(0, len(file_names_list)-1):
        merger = PdfFileMerger()
        while file_names_list[first_file_index].split(" - part", 2)[0] == file_names_list[first_file_index + counter].split(" - part", 2)[0]:
            merger.append(os.path.join(PATH, file_names_list[first_file_index]), 'rb')
            counter = counter + 1

        # Write the last files' appends to a new file
        merger.write(os.path.join(PATH, "results", file_names_list[first_file_index].split(" - part", 2)[0] + ".pdf"))
        #merger.close()
        first_file_index = first_file_index + counter
        counter = 0

    ''' for file_name in file_names_list:
        if file_name != previous_file_name:
            file_name_without_part = file_name.split(" - part", 2)
            if previous_file_name == "" or previous_file_name.startswith(file_name_without_part[0]):
                merger.append(os.path.join(PATH, file_name), 'rb')
            else:
                merger.append(os.path.join(PATH, file_name), 'rb')

                # Write all the appends to a new file
                merger.write(os.path.join(PATH, previous_file_name.split(" - part", 2)[0] + ".pdf"))
            previous_file_name = file_name '''


def main():
    '''Main function'''
    file_names_list = parsepdfsfile.parse_file(PATH)
    parsepdfsfile.remove_non_pdf_files(file_names_list)

    merge_pdf_files(file_names_list)

main()
