__author__ = 'wylitu'
import os
import sys

def displayFile(file):
    newname = file[0:file.rfind('.')] + '.py'
    command = "python -u D:\tools\uncompyle2\uncompyle2-master\scripts\uncompyle2 " + file + ">" + newname
    try:
        os.system(command)
    except Exception as e:
        print file

if __name__ == '__main__':

    #print unPath
    print 'init'
    displayFile('E:\\test.pyc')
    print 'finished'