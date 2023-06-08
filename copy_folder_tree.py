"""  This is to copy the folder structure without files """

import shutil
import os
import argparse

def get_user_inputs():
    """Gets the inputs from user (Source Directory and Destination Directory)

    Returns:
        Items: Source and Destination folder inputs
    """    
    argparser = argparse.ArgumentParser(
            prog='copy_folder_tree',
            description='Copy folder Tree')
    argparser.add_argument('src', type=str, nargs=1,
                            help='Source folder')
    argparser.add_argument('dest', type=str, nargs=1,
                            help='Destination folder')

    args = argparser.parse_args()
    return (args.src[0], args.dest[0])

def get_files(dir, content):
    """To get the files if present in given folder

    dir:
        dir (String): Folder
        files (String): content under the folder

    Returns:
        list : Files in given directory
    """
    return [f for f in content if os.path.isfile(os.path.join(dir, f))]

def copy_tree(src, dest):
    """Copies source folder to destination folder without files

    Args:
        src (String): Source folder
        dest (String): Destination folder
    
    Exception:
        Prints the message if destination folder already exists.

    """
    try:
        shutil.copytree(src, dest, ignore=get_files)
    except FileExistsError:
        print('The directory already exists')

src, dest = get_user_inputs()
copy_tree(src, dest)
