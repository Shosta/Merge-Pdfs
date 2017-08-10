'''
Hello
'''
#!/usr/bin/python3

import sys
import os.path
import parsepdfsfile




def merge_pdf_files(file_names_list):
	# Create a PdfFileMerger object.
    from PyPDF2 import PdfFileMerger
    first_file_index = 0
    counter = 0

    # Go through all elements of the list.
    while first_file_index < len(file_names_list):
        merger = PdfFileMerger()
        # Before appending the file, be sure that you are not testing above the list's last item.
        while first_file_index + counter <len(file_names_list) and file_names_list[first_file_index].split(" - part", 2)[0] == file_names_list[first_file_index + counter].split(" - part", 2)[0]:
            merger.append(os.path.join(directory_path, file_names_list[first_file_index + counter]), 'rb')
            counter = counter + 1

        # Write the last files' appends to a new file
        merger.write(os.path.join(directory_path, MERGED_PDFS_FOLDER, file_names_list[first_file_index].split(" - part", 2)[0] + ".pdf"))
        merger.close()
        # Add the counter to the first_file_counter to go to the next file.
        first_file_index = first_file_index + counter
        counter = 0


def main():
    '''Main function'''
    try:
        target_folder = sys.argv[1]
    except IndexError:
        print("Please write the directory path where you want to merge the pdfs as "
              "the first argument of the python call.\n"
              "At the moment, the files are going to be merged into the current folder.")
        target_folder = "."

    file_names_list = parsepdfsfile.parse_file(target_folder)
    parsepdfsfile.remove_non_pdf_files(file_names_list)

    merge_pdf_files(target_folder, file_names_list)


main()
