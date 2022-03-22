import pyodbc 
import shutil 
import subprocess
import os, stat
from pathlib import Path

def repo(i):
    switcher={
              'ASAP! LC':'ba04639-asap-lc',
              'DEPOT':'ba04639-depot',
              'DLA':'ba04639-dla',
              'ENGASJEMENT':'ba04639-engasjement',
              'IDENTITY_MANAGER':'ba04639-identity_manager',
              'KUNDE':'ba04639-kunde',
              'PARKERT':'ba04639-parkert',
              'PRODUKT':'ba04639-produkt',
              'RAMME':'ba04639-ramme',
              'RAMMEVERK':'ba04639-rammeverk',
              'SAK':'ba04639-sak',
              'VALUTA':'ba04639-valuta', 
    }   
    return switcher.get(i,"Invalid application")

Mode = 'PROD'
if Mode == 'PROD':
   SrcPath='X:\\Felix\\Prod\\'
   WikiSrcPath='\\\\dutap135\\FelixWiki\\data\\pages\\felix\\tjenester\\Program\\Prod'
   gitcmtmsg = "-m'Initial Load'"
   RexxSrcPath='X:\\Tools\Bin'
if Mode == 'Atest':  
   SrcPath='X:\\Felix\\Atest\\'
   WikiSrcPath='\\\\dutap135\\FelixWiki\\data\\pages\\felix\\tjenester\\Program\\Atest'
   gitcmtmsg = "-m'Atest Code'"
   RexxSrcPath='X:\\Tools\Bin' 
if Mode == 'Test':  
   SrcPath='X:\\Felix\\Test\\'
   WikiSrcPath='\\\\dutap135\\FelixWiki\\data\\pages\\felix\\tjenester\\Program\\test'
   gitcmtmsg = "-m'SIT Code'"
   RexxSrcPath='X:\\Tools\Bin' 
applconfpath='G:\\Felix Infra\\Zagility'      
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
    # applpath=appl.replace('!','').lower().replace(' ','-')
    applpath=repo(appl)
    # if appl == 'RAMMEVERK':
    #    applpath='r4639-sentralinfrastrukturfelix-cbl'
    print(appl)
    print('======')
    if len(appl)>1 and appl=='RAMMEVERK':
       curar = cnx2.cursor()
       curar.execute("SELECT * from dbo.AREA where APPLICATION ='"+appl+"' ;") 
       arearow = curar.fetchone()
       while arearow:
           print (arearow[0])
           area=str(arearow[0])
           arealc=area.lower()
           for path in Path(SrcPath+"Assembler").glob("*"+area+"*"):
               dest_dir=DstPath+applpath+'\\Assembler'
               shutil.copy(path, dest_dir)
               head_tail = os.path.split(path)
               destpath = dest_dir+'\\'+head_tail[1]               
               os.chmod(destpath, stat.S_IWRITE)
           for path in Path(SrcPath+"BMS").glob("*"+area+"*"):
               dest_dir=DstPath+applpath+'\\BMS'
               shutil.copy(path, dest_dir)
               head_tail = os.path.split(path)
               destpath = dest_dir+'\\'+head_tail[1]               
               os.chmod(destpath, stat.S_IWRITE)               
           for path in Path(SrcPath+"Cobol").glob("*"+area+"*"):
               dest_dir=DstPath+applpath+'\\Cobol'    
               head_tail = os.path.split(path)
               if head_tail[1].find('COBOL') == -1 and head_tail[1].find('grp') == -1 :
                  shutil.copy(path, dest_dir) 
                  destpath = dest_dir+'\\'+head_tail[1]               
                  os.chmod(destpath, stat.S_IWRITE)                             
           for path in Path(SrcPath+"Copylib").glob("*"+area+"*"):
               dest_dir=DstPath+applpath+'\\Copylib'
               shutil.copy(path, dest_dir)     
               head_tail = os.path.split(path)
               destpath = dest_dir+'\\'+head_tail[1]               
               os.chmod(destpath, stat.S_IWRITE) 
           # Added to include LIXX0000 & RIXX0000                
           if appl == 'RAMMEVERK':
               for path in Path(SrcPath+"Copylib").glob("*"+IXX00+"*"):
                   dest_dir=DstPath+applpath+'\\Copylib'
                   shutil.copy(path, dest_dir)     
                   head_tail = os.path.split(path)
                   destpath = dest_dir+'\\'+head_tail[1]               
                   os.chmod(destpath, stat.S_IWRITE)

           for path in Path(SrcPath+"Panels").glob("*"+area+"*"):
               dest_dir=DstPath+applpath+'\\Panels'
               shutil.copy(path, dest_dir) 
               head_tail = os.path.split(path)
               destpath = dest_dir+'\\'+head_tail[1]               
               os.chmod(destpath, stat.S_IWRITE)               
           for path in Path(SrcPath+"Versioning").glob("*"+area+"*"):
               dest_dir=DstPath+applpath+'\\Versioning'
               shutil.copy(path, dest_dir)                
        #    for path in Path(WikiSrcPath).glob("*"+arealc+"*"):
        #        dest_dir=DstPath+applpath+'\\Wiki'
        #        shutil.copy2(path, dest_dir)     
        #        head_tail = os.path.split(path)
        #        destpath = dest_dir+'\\'+head_tail[1]               
        #        os.chmod(destpath, stat.S_IWRITE)                          
           for path in Path(SrcPath+"XSD").glob("*"+area+"*"):   
               dest_dir=DstPath+applpath+'\\XSD'
               shutil.copy(path, dest_dir) 
               head_tail = os.path.split(path)
               destpath = dest_dir+'\\'+head_tail[1]               
               os.chmod(destpath, stat.S_IWRITE)               
           if appl == 'RAMMEVERK' and Mode == 'PROD':  
               for path in Path(SrcPath+"MACLIB").glob("*"):
                   dest_dir=DstPath+applpath+'\\MACLIB'
                   shutil.copy(path, dest_dir) 
                   head_tail = os.path.split(path)
                   destpath = dest_dir+'\\'+head_tail[1]               
                   os.chmod(destpath, stat.S_IWRITE)                   
               for path in Path(RexxSrcPath).glob("*.rex"):
                   dest_dir=DstPath+applpath+'\\Rexx'
                   shutil.copy(path, dest_dir) 
                   head_tail = os.path.split(path)
                   destpath = dest_dir+'\\'+head_tail[1]               
                   os.chmod(destpath, stat.S_IWRITE) 
           if Mode == 'PROD':   
               for path in Path(applconfpath).glob("*"):
                   dest_dir=DstPath+applpath+'\\application-conf'
                   shutil.copy(path, dest_dir) 
                   head_tail = os.path.split(path)
                   destpath = dest_dir+'\\'+head_tail[1]               
                   os.chmod(destpath, stat.S_IWRITE)                                                          
           arearow=curar.fetchone()
       Git=DstPath+applpath
       if os.path.exists(Git):
          os.chdir(Git)
          wd = os.getcwd()       
          p=subprocess.run(["git", "add", "*"], check=True, stdout=subprocess.PIPE).stdout
          print(p)
          p=subprocess.run(["git", "commit", gitcmtmsg], check=True, stdout=subprocess.PIPE).stdout
          print(p)
          p=subprocess.run(["git", "push"], check=True, stdout=subprocess.PIPE).stdout
          print(p)          
          p=subprocess.run(["git", "log"], check=True, stdout=subprocess.PIPE).stdout
          print(p)                                                                                                                   
    applrow = curap.fetchone()

