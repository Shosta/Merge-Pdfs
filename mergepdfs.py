'''
Main module for the 'mergepdfs.py' program.
It manage the command and arguments and the pdf merging in a file.
'''
import sys
import getopt
import os.path
import parsepdfsfile

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
    if separator == '':
        separator = ' - part'

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


#TODO: Move the main call and the sys arguments management into a specific file.
def usage():
    '''
    Display the awaited command and arguments for the 'mergepdfs.py'.
    '''
    print('mergepdfs.py -t <target_folder> -s <separator>')
    print('Default folder is the current folder.')
    print('Default separator is \' - part\'.')


def main(argv):
    '''Main function'''
    target_folder = ''
    separator = ''
    try:
       opts, args = getopt.getopt(argv,"ht:s:",["help=", "target_folder=","separator="])
    except getopt.GetoptError:
        print('Type \'mergepdfs.py -h\' for help.')
        sys.exit(2)

    if opts.__len__() == 0:
        usage()
        target_folder = '.'
        separator = ' - part'

    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ("-t", "--target_folder"):
            target_folder = arg
        elif opt in ("-s", "--separator"):
            if arg != '':
                separator = arg
            else:
                print('Default separator')
                separator = ' - part'
    print('Target Folder is: \"' + target_folder + "\"")
    print('Separator is: \"' + separator + "\"")
    

    # Parse the files.
    file_names_list = parsepdfsfile.parse_file(target_folder)
    file_names_list = parsepdfsfile.remove_non_pdf_files(file_names_list)

    # Merge the files.
    create_default_results_folder(target_folder)
    merge_pdf_files(target_folder, file_names_list, separator)

    print('Files merged successfully')

if __name__ == "__main__":
    main(sys.argv[1:])
