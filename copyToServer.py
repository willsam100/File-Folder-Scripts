#!/usr/bin/python -tt

import shutil
import os
import re
import sys
import time
import subprocess
##########################################
def itemExits(fullPath, result, isCopy):
  if os.path.exists(result):
    if os.path.getsize(fullPath) != os.path.getsize(result):
      string = 'Item already exists: ' + os.path.basename(full_path) + ' replace?'
      if askUser(string):
        transferItems(fullPath, result, isCopy)
    else:
      print 'Not copying ' + os.path.basename(fullPath), 'already exits!'
  else:
    transferItems(fullPath, result, isCopy)

##########################################
def askUser(string):
  print string, '[y/n]'
  answer = raw_input()
  if answer.startswith('n'):
      return False
  return True

##########################################

def shouldTransferFile(file, currentDir):
  # print 'checking if should transfer file', file
  if file[0] == '.':
    return False
  
  full_path = os.path.join(currentDir, file)
  
  # for openFile in listOfOpenFiles:
#     if full_path == openFile:
#       print 'File is being used, skipping'
#       return False
  
  size_mb = os.path.getsize(full_path) / 1000 / 1000
  
  if (size_mb < 100):
      if not askUser('File size is small ' + str(size_mb) + 'MB for: ' + file + ' copy anyway?'):
        return False
  return True

##########################################

def transferItems(current, result, isCopy):
    if isCopy:
        print 'copying', os.path.basename(current), 'to', result
        shutil.copy(current, result)
    else:
        print 'moving', os.path.basename(current), 'to', result
        shutil.move(current, result)

###########################################
def main():
  
  args = sys.argv
  
  dest_is_mounted = os.path.exists(destination)
  if not dest_is_mounted:
      call(['open', '/Users/willsam100/Desktop/MountServers.app/'])
      #time.sleep(5)
      print 'Mounting server'
      sys.exit(0)
  
  isCopy = False
  for i in args:
    if i == 'copy':
      print 'Setting mode to copy items!'
      isCopy = True
      args.remove('copy')
  if not isCopy:
    isCopy = askUser('Do you want to copy items?')
      
  
  isFile = ''
  currentDir = '/Users/willsam100/Desktop/Junk/Completed/'
  destination = '/Volumes/Media/TelevisionSeries/'
  destination_movie = '/Volumes/Media/Movies/'
  if len(args) == 2:
      currentDir = sys.argv[1]
      print destination
  
 
  
  # listOfOpenFiles = getData()
#   print listOfOpenFiles
#   print 'Exiting early'
#   sys.exit(0)

  #read in the files in the dir, check they are files and look for the seires trademark
  list_of_files = [f for f in os.listdir(currentDir) if shouldTransferFile(f, currentDir)]
  
  for inputFile in list_of_files:
    isSeries = re.search(r'S\d\de\d\d', os.path.basename(inputFile))
    if isSeries:
      programs = os.listdir(destination)
      for outputDir in programs:
        if outputDir == isSeries.string[0:isSeries.start()-1]:
          result = os.path.join(os.path.join(destination, outputDir), inputFile)
          current = os.path.join(currentDir, inputFile)
          itemExits(current, result, isCopy)

    else:
      if not os.path.isdir(inputFile):
        new_file = os.path.join(destination_movie, inputFile)
        current = os.path.join(currentDir, inputFile)
        itemExits(current, new_file, isCopy)
  print 'Completed'



if __name__ == '__main__':
  main()
