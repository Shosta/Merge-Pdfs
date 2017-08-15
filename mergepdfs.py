'''
Main module for the 'mergepdfs.py' program.
It manages the command and arguments and the pdf files merging in a single file as
long as the file as properly named.
'''
import sys
import getopt
import mergefiles
import parsepdfsfile


def usage():
    '''
    Display the awaited command and arguments for the 'mergepdfs.py'.
    '''
    print('Here is the default usage of that command:')
    print('mergepdfs.py -f <source_folder> -s <separator>')
    print('We don\'t detect any folder and so we are selecting the default folder is the '
          'current folder.')
    print('We don\'t detect any folder and so we are selecting the default separator is '
          '\' - part\'.')


def main(argv):
    '''Main function'''
    source_folder = '.'
    separator = ' - part'
    try:
        opts, args = getopt.getopt(argv, "hf:s:", ["help=", "source_folder=", "separator="])
    except getopt.GetoptError:
        print('Type \'mergepdfs.py -h\' for help.')
        sys.exit(2)

    if opts.__len__() == 0:
        usage()

    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ("-f", "--source_folder"):
            source_folder = arg
        elif opt in ("-s", "--separator"):
            separator = arg
    print('Target Folder is: \"' + source_folder + "\"")
    print('Separator is: \"' + separator + "\"")


    # Parse the files.
    file_names_list = parsepdfsfile.parse_file(source_folder)
    file_names_list = parsepdfsfile.remove_non_pdf_files(file_names_list)

    # Merge the files.
    mergefiles.create_default_results_folder(source_folder)
    mergefiles.merge_pdf_files(source_folder, file_names_list, separator)

    print('Files merged successfully')


if __name__ == "__main__":
    main(sys.argv[1:])
