"""  Python – Copy Directory Structure Without Files """

import shutil
import os
import argparse

def user_input():
    """To get inputs from user :- Source Directory and Destination Directory

    Returns:
        String: Source and Destination converted from list to string 
    """    
    argparser = argparse.ArgumentParser(
            prog='create_folders_without_files',
            description='Copy Directory Structure Without Files')
    argparser.add_argument('sourcedirectory', type=str, nargs=1,
                            help='Directory Structure With Files')
    argparser.add_argument('destdirectory', type=str, nargs=1,
                            help='Directory Structure Without Files')

    args = argparser.parse_args()
    srcdirectory = args.sourcedirectory[0]
    destdirectory = args.destdirectory[0]
    return (srcdirectory,destdirectory)

def ignore_files(dir, files):
    """To ignore the files if present in any folders

    dir:
        dir (String): Directory
        files (String): Files under the directory

    Returns:
        Directory(Full Path) : String Format
    """
    return [f for f in files if os.path.isfile(os.path.join(dir, f))]

def copy_without_files(srcdir, destdir):
    """Source Directory Structure copied to Destination Without Files

    Args:
        srcdirectory (String): Input from user - Source Directory with files
        destdirectory (String): Input from user - Destination Directory - Directory copied without Files
    
    Exception:
        Exception raised if Destination file already exists.

    """
    try:
        shutil.copytree(srcdir, destdir, ignore=ignore_files)
    except FileExistsError:
        print('The directory already exists')

#Get Source and Destination to generate the destination directory without files
s_directory, d_directory = user_input()
copy_without_files(s_directory, d_directory)
