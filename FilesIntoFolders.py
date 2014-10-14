#!/usr/bin/python -tt
# FilesIntoFolders
# Program to copy a file into a folder with the name of the file

import os
import sys
import re
import commands

def main():
  if len(sys.argv) != 2:
    sys.stderr.write('Fix the arguments, exting.....')
    sys.exit(1)
  root = sys.argv[1]

  isDir = os.path.isdir(root)
  if not isDir:
    sys.stderr.write('Augrument is not a direcotry', root)
    sys.exit(1)
 
  files = os.listdir(root)
  for file in files:
    isFile = os.path.isfile(os.path.abspath(os.path.join(root, file)))
    if isFile:
      (basename, ext) = os.path.splitext(file)
      if ext:
        basename = os.path.abspath(os.path.join(root, basename))
        mkdir = 'mkdir \'' + basename + '\''
        move = 'mv \'' + os.path.abspath(os.path.join(root, file)) + '\' \'' + os.path.abspath(os.path.join(basename, file)) + '\''
        (output, status) = commands.getstatusoutput(mkdir)
        if status:
	        sys.stderr.write('Error creating dir: ' + str(output) + '\n')
        else:
          print output, file
        (output, status) = ['','']
        (output, status) = commands.getstatusoutput(move)
        if status:
	        sys.stderr.write('Error moving file: ' + str(output) + '\n')
        else:
          print output, file
  sys.exit(0)

if __name__ == '__main__':
  main()
