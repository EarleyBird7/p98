import os
import shutil
source=input("Enter the name of the source folder")
destination=input("Enter the name of the destination folder")
source=source+"/"
destination=destination+"/"
fileList=os.listdir(source)
for file in fileList:
    shutil.copy((source+file), destination)