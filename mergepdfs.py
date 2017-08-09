'''

'''
import os.path
import string
import parsepdfsfile

# import sys 
# sys.argv[1] le premier argument de la commande lorsque l'on lance la commande depuis un terminal.

PATH = "C:\\Remi\\Developpement\\A traiter"
# PATH = 'C:\\Remi\\ShostaSync\\Scans a traiter'

from PyPDF2 import PdfFileMerger, PdfFileReader

def merge_pdf_files(file_names_list):

    merger = PdfFileMerger()
    previous_file_name = ''

    for file_name in file_names_list:
        if file_name != previous_file_name:
            file_name_without_part = file_name.split(" - part", 2)
            if previous_file_name == "" or previous_file_name.startswith(file_name_without_part[0]):
                merger.append(os.path.join(PATH, file_name), 'rb')
            else:
                merger.append(os.path.join(PATH, file_name), 'rb')

                # Write all the appends to a new file
                merger.write(os.path.join(PATH, previous_file_name.split(" - part", 2)[0] + ".pdf"))

            previous_file_name = file_name

    # Write the last files' appends to a new file
    merger.write(os.path.join(PATH, file_name_without_part[0] + ".pdf"))


def main():
    '''Main function'''
    file_names_list = parsepdfsfile.parse_file(PATH)
    parsepdfsfile.remove_non_pdf_files(file_names_list)

    merge_pdf_files(file_names_list)

main()
