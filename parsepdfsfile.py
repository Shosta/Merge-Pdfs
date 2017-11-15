'''
Parse the files in a directory and return a sorted array of Pdf files in that directory.
'''

def parse_file(dir_path):
    '''
    Parse a directory and return an array that contains all the files in it.

    Params:
    dir_path: The Directory path where we want to retrieve the files.

    Return:
    A list of files from the directory in argument.
    '''
    from os import listdir
    from os.path import isfile, join
    only_files = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
    only_files.sort()

    return only_files

def remove_non_pdf_files(file_names_array):
    '''
    Remove all the non Pdf files from a list of file names.

    Params:
    files_array: The list of files names from which we want to remove the non Pdf files.

    Return:
    A list of files that contains only Pdf file names.
    '''
    result_array = []
    for file_name in file_names_array:
        if file_name.lower().endswith('.pdf'):
            result_array.append(file_name)

    return result_array
