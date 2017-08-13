'''
Merge together pdf files in a specified directory.
The files must be named properly to be identified as mergeable.
'''
import os.path

MERGED_PDFS_FOLDER = 'results'

def create_default_results_folder(directory_path):
    '''
    From the directory path passed as an argument, it checks if the MERGED_PDFS_FOLDER exists and creates it if not.

    Params:
    directory_path: The Directory path from where we want to check if the MERGED_PDFS_FOLDER exists.
    '''
    results_directory = os.path.join(directory_path, MERGED_PDFS_FOLDER)
    if not os.path.exists(results_directory):
        # Create default "results" path.
        os.makedirs(results_directory)


def merge_pdf_files(directory_path, file_names_list, separator):
    '''
    Check the Pdf files from the 'file_names_list' and merge the ones that are named as followed :
    'file name "separator"1.pdf'
    ...
    'file name - "separator"N.pdf'
    into a single Pdf file names 'file name.pdf'.

    The merged pdf files are then stored into the 'MERGED_PDFS_FOLDER'.

    Params:
    directory_path: The path from where the function is going to merge the Pdf files.
    file_names_list: A list that contains all the name of the Pdf files we want to merge.
    '''
	# Create a PdfFileMerger object.
    from PyPDF2 import PdfFileMerger
    first_file_index = 0
    counter = 0

    # Go through all elements of the list.
    while first_file_index < len(file_names_list):
        merger = PdfFileMerger()
        # Before appending the file, be sure that you are not testing above the list's last item.
        while first_file_index + counter <len(file_names_list) and file_names_list[first_file_index].split(separator, 2)[0] == file_names_list[first_file_index + counter].split(separator, 2)[0]:
            merger.append(os.path.join(directory_path, file_names_list[first_file_index + counter]), 'rb')
            counter = counter + 1

        # Write the last files' appends to a new file
        merger.write(os.path.join(directory_path, MERGED_PDFS_FOLDER, file_names_list[first_file_index].split(separator, 2)[0] + ".pdf"))
        merger.close()
        # Add the counter to the first_file_counter to go to the next file.
        first_file_index = first_file_index + counter
        counter = 0
