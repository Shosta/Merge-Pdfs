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
    mergefiles.create_default_results_folder(target_folder)
    mergefiles.merge_pdf_files(target_folder, file_names_list, separator)

    print('Files merged successfully')

if __name__ == "__main__":
    main(sys.argv[1:])
