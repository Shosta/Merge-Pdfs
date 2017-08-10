'''
Hello
'''
#!/usr/bin/python3

import os.path
import parsepdfsfile


# import sys
# sys.argv[1] le premier argument de la commande lorsque l'on lance la commande depuis un terminal.

#PATH = "C:\\Remi\\Developpement\\A traiter"
PATH = "/Users/Shosta/Developpement/A traiter"
# PATH = 'C:\\Remi\\ShostaSync\\Scans a traiter'

def merge_pdf_files(file_names_list):
	# Create a PdfFileMerger object.
    from PyPDF2 import PdfFileMerger
    first_file_index = 0
    counter = 0

    # Go through all elements of the list.
    while first_file_index < len(file_names_list):
        merger = PdfFileMerger()
        # Before appending the file, be sure that you are not testing above the list last item.
        while first_file_index + counter <len(file_names_list) and file_names_list[first_file_index].split(" - part", 2)[0] == file_names_list[first_file_index + counter].split(" - part", 2)[0]:
            merger.append(os.path.join(PATH, file_names_list[first_file_index + counter]), 'rb')
            counter = counter + 1

        # Write the last files' appends to a new file
        merger.write(os.path.join(PATH, "results", file_names_list[first_file_index].split(" - part", 2)[0] + ".pdf"))
        merger.close()
        # Add the counter to the first_file_counter to go to the next file.
        first_file_index = first_file_index + counter
        counter = 0


def main():
    '''Main function'''
    file_names_list = parsepdfsfile.parse_file(PATH)
    parsepdfsfile.remove_non_pdf_files(file_names_list)

    merge_pdf_files(file_names_list)

main()
