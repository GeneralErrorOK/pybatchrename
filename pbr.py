# Small commandline utility to batch rename all files in a directory.
#
# Usage: pbr -fb <string> <directory>
# -p: place string of characters in front of exisiting filename
# -s: place string of characters after existing filename (but before extension)
#
# Creator: Willem van de Kletersteeg
# Date: September 2018

import os
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="Batch rename files in a directory by adding prefix or suffix text.", prog="PyBatchRename (pbr)")
group = parser.add_mutually_exclusive_group()
group.add_argument('-p', help="Insert given text as prefix", action="store_true")
group.add_argument('-s', help="Insert given text as suffix", action="store_true")
parser.add_argument('renamestring', metavar="RENAMESTRING", help="Text to insert into filenames.")
parser.add_argument('dirname', metavar="DIRECTORY", default=".", help="Directory to apply renames to.")

arguments = parser.parse_args()

workingdir = Path(arguments.dirname)
if workingdir.is_dir() and workingdir.exists():
    files = os.listdir(workingdir)
    for old_file_name in files:
        if arguments.p:
            new_file_name = arguments.renamestring + old_file_name
        if arguments.s:
            splittedFilename = old_file_name.split(".")
            new_file_name = splittedFilename[0] + arguments.renamestring + splittedFilename[1]
    
        os.rename(Path(workingdir.joinpath(old_file_name)), Path(workingdir.joinpath(old_file_name)))
