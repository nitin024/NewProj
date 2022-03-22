import pyodbc 
import shutil 
from pathlib import Path

SrcPath='X:\\Felix\\Prod\\'
WikiSrcPath='\\\\dutap135\\FelixWiki\\data\\pages\\felix\\tjenester\\Program\\Prod'
RexxSrcPath='X:\\Tools\Bin'
DstPath='C:\\Git\\'
server = 'tcp:dutap135.udnbnor.net' 
database = 'FelixDD' 
username = 'qryFelixDD' 
password = '' 
cnxn = pyodbc.connect('Driver={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD=')
cnx2 = pyodbc.connect('Driver={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD=')
curap = cnxn.cursor()

curap.execute("SELECT * from dbo.APPLICATION ;") 
applrow = curap.fetchone() 
while applrow:
    appl=applrow[0]
    appl=appl.strip() 
    print(appl)
    print('======')
    if len(appl)>1:
       curar = cnx2.cursor()
       curar.execute("SELECT * from dbo.AREA where APPLICATION ='"+appl+"' ;") 
       arearow = curar.fetchone()
       while arearow:
           print (arearow[0])
           area=str(arearow[0])
           arealc=area.lower()
           for path in Path(SrcPath+"Assembler").glob("*"+area+"*"):
               dest_dir=DstPath+appl+'\\Assembler'
               shutil.copy(path, dest_dir)
           for path in Path(SrcPath+"BMS").glob("*"+area+"*"):
               dest_dir=DstPath+appl+'\\BMS'
               shutil.copy(path, dest_dir)
           for path in Path(SrcPath+"Cobol").glob("*"+area+"*"):
               dest_dir=DstPath+appl+'\\Cobol'
               shutil.copy(path, dest_dir)                   
           for path in Path(SrcPath+"Copylib").glob("*"+area+"*"):
               dest_dir=DstPath+appl+'\\Copylib'
               shutil.copy(path, dest_dir)                   
           for path in Path(SrcPath+"Panels").glob("*"+area+"*"):
               dest_dir=DstPath+appl+'\\Panels'
               shutil.copy(path, dest_dir) 
           for path in Path(SrcPath+"Versioning").glob("*"+area+"*"):
               dest_dir=DstPath+appl+'\\Versioning'
               shutil.copy(path, dest_dir)                
           for path in Path(WikiSrcPath).glob("*"+arealc+"*"):
               dest_dir=DstPath+appl+'\\Wiki'
               shutil.copy(path, dest_dir)                
           for path in Path(SrcPath+"XSD").glob("*"+area+"*"):   
               dest_dir=DstPath+appl+'\\XSD'
               shutil.copy(path, dest_dir) 
           if appl = 'RAMMEVERK':  
               for path in Path(SrcPath+"MACLIB").glob("*"):
                   dest_dir=DstPath+appl+'\\MACLIB'
                   shutil.copy(path, dest_dir) 
               for path in Path(RexxSrcPath).glob("*.rex"):
                   dest_dir=DstPath+appl+'\\Rexx'
                   shutil.copy(path, dest_dir)                     
           arearow=curar.fetchone()                                                                                                            
    applrow = curap.fetchone()
    