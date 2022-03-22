# Importing module 
import shutil 
import errno 
import os.path
from os import path

# Input the Source path 
print("-------------------------------")
print("¤¤ COPY PROGRAM TO WORKSPACE ¤¤")
print("-------------------------------")
print("Select Input Path - ")
print("1 : UTV")
print("2 : SIT")
print("3 : PROD")
Region = input('** Input : ')
if Region == '1':
   print("Copying from UTV --> ")
   srcfile = "X:\\Felix\\Utvikling\\Utvikling\\Cobol\\"
elif Region == '2':
   print("Copying from SIT --> ")
   srcfile = "X:\\Felix\\Test\\Cobol\\"
elif Region == '3':
   print("Copying from PROD --> ")
   srcfile = "X:\\Felix\\Prod\\Cobol\\"
else:
   print("Incorrect selection. Program EXIT.")
   quit()

# Destination path 
dest = "U:\\Projects\\workspace\\NkED1Proj\\CobolCopy\\"
#print("Destination : " + dest)
print('')

pgm = input('** Input Program Name : ')
pgm = pgm.upper()

srcpgm = srcfile + pgm + '.CBL'

# Check if file ixists
if  path.exists(srcpgm) :
   #print("Input file " + srcpgm + " exists")
   #copy2 to copy the permissions as well
   shutil.copy2(srcpgm,dest)
   #copyfile to make file editable
   #shutil.copyfile(srcpgm,dest)
   print('Program ' + pgm + '.CBL Copied.')
else:
   print("Input file " + srcpgm + " does NOT exists")
   
# Copy the content of 
# source to destination 