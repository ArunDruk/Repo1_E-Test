import os

from datetime import datetime

print(os.getcwd())  # Get Current working directory
os.chdir("F:\Doc's") # Change the directory to different path
print(os.getcwd())
#try:
   # os.mkdir("F:\Doc's\Created3")  # Make/create directory
#os.rmdir("F:\Doc's\Created2")   # Deletes/removes sub directory or a folder directory
#os.makedirs("F:\Doc1's\Sub_Created5") # This makedirs creates the main and sub folders if it is not present, mkdir will give error if the main folder not present.
#os.removedirs("F:\Doc1's\Sub_Created5") # This removes/deletes the main and sub folders inside it.
#except FileExistsError:
    #print("File/folder with same name already exists")
#os.rename("Created3","Renamed3") # renames the directory / files
#os.rename("TECHMAHINDRA_Resignation_Acceptance_Letter.PDF","TechM_Acceptance_resignation.PDF") # Here it renames the file
#print(os.stat("Renamed3")) # os.stat("filename") gives the information on the file like size, modified time
time_stamp=os.stat("Renamed3").st_mtime
print(datetime.fromtimestamp(time_stamp)) # Printing the timestamp of the file modified.
print(datetime.now().time()) # To print current time
#print(os.listdir())  # Lists directory