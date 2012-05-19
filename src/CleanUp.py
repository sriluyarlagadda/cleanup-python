'''
Created on May 12, 2012

@author: Srilu
'''

from argparse import ArgumentParser
import os




files_list = []
def getAllFilesFromDir(directory, recursive = True):
    print(directory)    
    if(os.access(directory, os.R_OK)):   
         for dir_path, dir_names, files_names in os.walk(directory):
            if(files_names):
                for file_name in files_names:
                    files_list.append(os.path.join(dir_path, file_name))
            if(dir_names):
                for dir in dir_names:
                    #print(file)     
                    if(dir[:1]  in  ('.', '$')):
                        pass
                    else:
                        if(recursive):
                            getAllFilesFromDir(os.path.join(dir_path, dir))
        



    #get all the files from the directory 'dir'
def getOldFilesFromDir(dir):
    #if directory is null assume it as current
    #contains all directories which should not be scanned
    settings = []    
    getAllFilesFromDir(dir, False)
    print(files_list)
    for file in files_list:
        pass
        #check if it is old last accessed
    print(files_list)
    
    
    
#main control loop
def main():
    #print(os.curdir)
    parser_cleanup = ArgumentParser()
    #parser_cleanup.add_argument("--dir", default = True)
    parser_cleanup.add_argument("--old", help = "display old files", action = "store_true")
    options = parser_cleanup.parse_args()
    #get all old files
    if(options.old == True):
        dir_path = "C:/Call.of.Duty.4.Modern.Warfare.Full-Rip.Skullptura"
        if(os.path.exists(dir_path) and  os.path.isdir(dir_path)):
            getOldFilesFromDir(dir_path)
        else:
            print("it is not a valid directory")
            exit;
        
        
        
#execution starts        
main()
    
    
    
