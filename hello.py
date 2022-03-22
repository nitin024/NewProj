print('Hello, world!')

srcfile = "C:\\temp\\"

#pgm = input('Input Program Name : ')
file1 = 'demofilepython.txt'
srcpgm = srcfile + file1
print(f'File Path: {srcpgm}')

print('**** Content of the file :')
f = open(srcpgm, "r")
#print(f.read())
for x in range(6):
    print(f.readline())
    x +=1
    
