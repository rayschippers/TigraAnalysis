__author__ = 'raymond'
import os
def ifdirexists (directory):
    if os.path.exists(directory):
        if os.path.isdir(directory):
                return 'true'
        else:
                return 'false'
    else:
         print("Path does not exist")
         return 'false'