# Simplified version 
import os
from extensionsWDEY import extension_paths

def sortFilesInDirectory(currentDirectory):
    # If currentDirectory does not exist return
    if not os.path.exists(currentDirectory):
        return
    
    filesInCurrentDirectory = os.listdir(currentDirectory)
    for _file in filesInCurrentDirectory:
        # TODO: CHECK FILE NAME TO BE VALID FIRST...
        if "$" not in _file:
            # Get extention of file and make lower case
            extension = os.path.splitext(_file)[1]
            extension = extension.lower()
            
            # If the extention is a know extention
            if extension in extension_paths:
                
                # Path to file 
                currentPath2file = currentDirectory + "\\" + _file
                
                # New path (destination) and path to file
                destinationPath = currentDirectory + "\\" + extension_paths[extension] 
                destinationPath2file = destinationPath + "\\" + _file
                
                # Does the destination exist ?
                pathExists = os.path.exists(destinationPath)
                if pathExists: # If yes just move file
                    os.replace(currentPath2file, destinationPath2file)
                    print("Moved!!!")
                    
                else: # If no make the directory and move the file
                    os.mkdir(destinationPath)
                    os.replace(currentPath2file, destinationPath2file)
                    print("Directory made and file moved!!!")


if __name__ == "__main__":
        
    downloadsfolder = ''
    newDirectory = downloadsfolder
    sortFilesInDirectory(downloadsfolder);
