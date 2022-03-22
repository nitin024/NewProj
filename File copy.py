# Importing module 
import shutil 
import errno 
  
# Source path 
src = 'C:\Felix\Tools\rexx.rex'
  
# Destination path 
dest = 'C:\Felix\Tools\bin'
  
# Copy the content of 
# source to destination 
try: 
    shutil.copytree(src, dest) 
    shutil.copy
except OSError as err: 
  
    # error caused if the source was not a directory 
    if err.errno == errno.ENOTDIR: 
        shutil.copy2(src, dest) 
    else: 
        print("Error: % s" % err)
        
        
        
# Modern way to open files. The closing in handled cleanly
with open('IXODBSTP', mode='r') as in_file, \
     open('IXODBSTP.txt', mode='w') as out_file:

    # A file is iterable
    # We can read each line with a simple for loop
    for line in in_file:

        # Tuple unpacking is more Pythonic and readable
        # than using indices
        ref, name, price, quantity, reorder = line.split()

        # Turn strings into integers
        quantity, reorder = int(quantity), int(reorder)

        if quantity <= reorder:
            # Use f-strings (Python 3) instead of concatenation
            out_file.write(f'{ref}\t{name}\n')        
