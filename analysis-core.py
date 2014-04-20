__author__ = 'raymond'
import os
import magic
import re
import hashfile
import filepatcheck
DEBUGFLAG = 0
FILEDIR = '/Users/raymond/malware'
PROCESSEDFILEDIR = '/Users/raymond/complete'
def anaylsiscore():
    for subdir, directories, filenames in os.walk(FILEDIR):
                 for filename in filenames:
                        stringsInfile = "none"
                        #Create the full file path to pass into libmagic (via python-magic)
                        tempfile = os.path.join(subdir,filename)
                        filehash = hashfile.hashingfile(tempfile)
                        filetype = magic.from_file(tempfile)
                        filetypestring = filetype.decode(encoding='UTF-8')

                        #If the file is a executable run strings on it
                        if re.search("executable", filetypestring):
                            filetostring = open(tempfile, 'rb')
                            stringsInfile = filetostring.readline()
                            filetostring.close()

                        #output the detect filetype.
                        print("Filename:",tempfile)
                        print("File type: ",filetypestring)
                        print("Hash: ",filehash)
                        print("Strings: ", stringsInfile,'\n')
                        #to do:
                        #seen before?, submit to cuckoobox, VT
                        #seperate dbengine



#Test if file path exists
if filepatcheck.ifdirexists(FILEDIR) == 'true':
    print("Steo 1")
    if filepatcheck.ifdirexists(PROCESSEDFILEDIR) == 'true':
        anaylsiscore()
        print("Step 2")
else:
    print("It didn't work")

#walk through the directory and sub-directories specified in FILEDIR
