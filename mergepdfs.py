'''
Main module for the 'mergepdfs.py' program.
It manages the command and arguments and the pdf files merging in a single file as
long as the file as properly named.
'''
import sys
import getopt
import parsepdfsfile
import mergefiles


def usage():
    '''
    Display the awaited command and arguments for the 'mergepdfs.py'.
    '''
    print('Here is the default usage of that command:')
    print('mergepdfs.py -f <source_folder> -d <destination_folder> -s <separator>')
    print('If no source folder is specified, the default source folder is the '
          'current folder.')
    print('If no destination folder is specified, the default destination folder is the '
          'current folder.')
    print('Nevertheless, if the user specifies the source folder but not the destination folder,')
    print('then the destination folder is identical as the source folder.')
    print('If no file separator is specified, the default separator is  \' - part\'.')


def main(argv):
    '''Main function'''
    source_folder = '.'
    separator = ' - part'
    destination_folder = '.'
    try:
        opts, args = getopt.getopt(argv, "hf:d:s:", ["help=", "source_folder=", "destination_folder=", "separator="])
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
        elif opt in ("-d", "--destination_folder"):
            destination_folder = arg

    # If the user specify the source folder but not the destination folder,
    #then the destination folder is identical to the source folder.
    if source_folder != '.' and destination_folder == '.':
        destination_folder = source_folder

    print('Source folder is: \"' + source_folder + "\"")
    print('Destination folder is: \"' + destination_folder + "\"")
    print('File separator is: \"' + separator + "\"")

    # Parse the files.
    file_names_list = parsepdfsfile.parse_file(source_folder)
    file_names_list = parsepdfsfile.remove_non_pdf_files(file_names_list)

    # Merge the files.
    mergefiles.create_default_results_folder(destination_folder)
    mergefiles.merge_pdf_files(source_folder, destination_folder, file_names_list, separator)

    print('Your files are merged successfully.')


if __name__ == "__main__":
    main(sys.argv[1:])
