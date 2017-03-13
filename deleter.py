# -*- coding: utf-8 -*-
from lxml import objectify, etree
import xmltodict
from xml.dom import minidom
import time
import os
import xml.etree.ElementTree as ET
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time
i = 0

def selectiveDeleter(path):
    i = 0
    for root, dirs, files in os.walk(path, topdown=False):
        # print 'Files: '
        for name in files:
            #print(os.path.join(root, name))
            #print 'Name: ', name, 'Root: ', root
            filename = os.path.join(root, name)
            extension = os.path.splitext(filename)[1]
            filename_without_extension = os.path.splitext(name)[0]
            #toDo add logic for different extensions
            if extension == '.zip':
                print 'Deleting: ', filename
                os.unlink(filename)

if __name__ == "__main__":
    global path
    path = os.getcwd()
    selectiveDeleter(path)
