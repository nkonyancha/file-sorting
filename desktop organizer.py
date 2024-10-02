#a file sorting program sorting files into folders based of unique identifier

import os
import shutil   

path = input("enter path to be sorted: ")#ask for path to be sorted eg C:\Users\user\Documents\
files=os.listdir(path)

null=""
for file in files:
    filename,extension=os.path.splitext(file)
    extension=extension[1:]
    foldername=filename[0:3]#checks for unique identifier
    #first three letters should be unique identifier

    if extension!= null:#check if the file being worked on is a folder

        #subjects i want to group
        if foldername=="eng" or foldername=="MTH" or foldername=="bio":
            #this is line can be removed if you have a unique identifier for every file

            if os.path.exists(path+'/'+foldername):
                shutil.move(path+'/'+file,path+'/'+foldername+'/'+file)
                
            else:
            
                os.makedirs(path+'/'+foldername)
                shutil.move(path+'/'+file,path+'/'+foldername+'/'+file)
        else: 
            #sorting other files into one folder
            shutil.move(path+'/'+file,path+'/'+"DSA"+'/'+file)
    else:
        #skips folders
        print("skipped")


