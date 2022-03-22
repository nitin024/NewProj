# Importing module 
import shutil 
import errno 
import binascii
  
# Source path 
src = 'C:\IMS255\IXODBSTP'
  
# Destination path 
dest = 'C:\IMS255\IXODBSTP.txt'
  
#fi = open(src, "r")
#fo = open(dest, "w")
#print(fi.read())


# Modern way to open files. The closing in handled cleanly
#with open('NK1.txt', mode='rb') as in_file, \
#     open('NK1_out.txt', mode='w') as out_file:
#        text = in_file.read(1)
#        print(f'Text:  {text}')
#        data_b2a = binascii.b2a_uu(text)
#        print(f'ASCII :  {data_b2a}')
    ##out_file.write(" ".join(map(str,data)))
    
        #sentence = bytearray(data.encode("ascii"))
#        out_file.write(data_b2a)
    
    # A file is iterable
    # We can read each line with a simple for loop
    #for line in in_file:
        #print(line)
        #out_file.write(line)
        #out_file.write(" ".join(map(str,line)))
            #out_file.write("\n")
            
            

text = "Simply Easy Learning"

# Converting binary to ascii
data_b2a = binascii.b2a_uu(text)
print ("**Binary to Ascii** \n")
print (data_b2a)

# Converting back from ascii to binary 
data_a2b = binascii.a2b_uu(data_b2a)
print ("**Ascii to Binary** \n")
print (data_a2b)