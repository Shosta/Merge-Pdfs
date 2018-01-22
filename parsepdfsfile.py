'''
Parse the files in a directory and return a sorted array of Pdf files in that directory.
'''

import re
def natural_sort(list_to_sort):
    '''
    Sort the given list in the way that humans expect.
    '''
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    list_to_sort.sort(key=alphanum_key)


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
    natural_sort(only_files)

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
