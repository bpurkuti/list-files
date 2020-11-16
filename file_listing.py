# #File Listing

import os
#specify path/Also example path in a windows machine with bash terminal
#path = '/mnt/c/Users/Bishwo Purkuti/Documents/Python Stuff/MilanoTechChallenge/tests'
path = str(input())

#Main function
def listDir(dir):
    #Make a list of files in the directory specified by path
    filesList = os.listdir(dir)
    for f in filesList:
        #if possible, split the name and extension into seperate variables
        name, extension = os.path.splitext(f)
        #if the extension is .gps and first letter is A, print filename and its path
        if(extension=='.gps'):
            if(name[0]=='A'):
                print("File: " + f)
                #print absolute path of the given file
                print("File-path: " + os.path.abspath(f), '\n')

if __name__== '__main__':
    listDir(path)