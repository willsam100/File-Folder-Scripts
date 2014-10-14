#!/usr/bin/python -tt
import sys
import re
import os

#script to determine if the folder contains a DVD Structure

def main():
  if len(sys.argv) <= 1:
    print 'more args needed'
    sys.exit(1)

  print 'looking for dvds'
  files = []
  dvdFolders = []
  dir = sys.argv[1]
  if os.path.isdir(dir):
    files = os.listdir(dir)
  else:
    print 'error, folder is not a dir'
  
  for file in files:
    file = os.path.join(dir, file)
    subfiles = []
    if os.path.isdir(file):
      subfiles = os.listdir(file)
    
    for f in subfiles:
      match = re.match(r'VIDEO_TS', f,)
      if match:
        dvdFolders.append(os.path.basename(file))
      else:
        match = re.match(r'video_ts', f,)
        if match:
            dvdFolders.append(os.path.basename(file))

  if dvdFolders:
    for f in dvdFolders:
      print f
  else:
    print 'Not a dvd structure'

if __name__ == '__main__':
  main()
