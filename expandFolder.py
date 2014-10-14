#! /usr/bin/python
import os
import shutil

#script to remove video files of specific extenstions to supplied 
#destination
#Usage: dir_with_video_folders destination_for_videos

def main(path, destination, file_extenstion=None):
    if file_extenstion == None:
        file_extenstion = ['mp4','m4v', 'avi','mpg','MPG','divx', 'mkv']

    files_to_be_moved = os.listdir(path)
    findFilesInFolder(path, destination, file_extenstion, files_to_be_moved)


#def recurseFolder(path, destination, file_extenstion):
#   for d in os.listdir(path):
#       if os.path.isdir(os.path.join(path, d)) and not d == '3d'and not d[0] == '.':
#           folder = os.path.join(path, d)
#           files_to_be_moved = os.listdir(folder)
#           findFilesInFolder(d, path, destination, file_extenstion, files_to_be_moved)
    
    

def findFilesInFolder(path, destination, file_extenstion, files_to_be_moved):
   for tmp in files_to_be_moved: 
       print tmp
       if os.path.isdir(os.path.join(path, tmp)) and not tmp == '3d'and not tmp[0] == '.':
           files_to_be_moved = os.listdir(os.path.join(path, tmp))
           findFilesInFolder(os.path.join(path, tmp), destination, file_extenstion, files_to_be_moved)

       is_vaild_extenstion = False
       for ext in file_extenstion:
           if tmp.endswith(ext):
               is_vaild_extenstion = True
               break
       if is_vaild_extenstion:
           file_name = os.path.join(path, os.path.join(path, tmp))
           new_name = os.path.join(destination, tmp) 
           print tmp, new_name
           shutil.move(file_name, new_name)
           
if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 1:
        print 'Usage: python expandFolder dir [destination]'
        sys.exit(0)
    path = sys.argv[1]
    if len(sys.argv) > 2:
        destination = sys.argv[2]
    else:
        destination = sys.argv[1]

    main(path, destination)

