import PyQt5
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QSplashScreen, QDesktopWidget
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow

import os
import sys
import time
import urllib2
import json
sys.path.insert(0, os.getcwd() + r'\\plugins\\Updater')
dn = os.getcwd()


#python
req = urllib2.Request("https://api.github.com/repos/x64dbg/x64dbgpy/releases/latest")
opener = urllib2.build_opener()
f = opener.open(req)
json = json.loads(f.read())
#print json debug only
branch = json[u'name']
#print branch
first_up = "https://github.com/x64dbg/x64dbgpy/releases/download/"
reg2 = first_up + branch +"/"+ "x64dbgpy-"+ branch+".zip"
#print reg2
build_date = reg2
file_name = reg2.split('/')[-1]
u = urllib2.urlopen(reg2)

#x64dbg
zeq = urllib2.Request("https://api.github.com/repos/x64dbg/x64dbg/releases/latest")
zopener = urllib2.build_opener()
zf = zopener.open(zeq)
#print zf
import json
json = json.loads(zf.read())
#print json
#print json debug only
zbranch = json[u'name']
#print zbranch
zfirst_up = "https://github.com/x64dbg/x64dbg/releases/download/snapshot/"
zreg2 = zfirst_up + zbranch
zbuild_date = zreg2
zfile_name = zreg2.split('/')[-1]
zu = urllib2.urlopen(zreg2)

def X64dbgSplash(self):
    ############################################
    splash2 = PyQt5.QtWidgets.QSplashScreen(QtGui.QPixmap("22.png"), QtCore.Qt.WindowStaysOnTopHint)
    font2 = splash2.font()
    font2.setPixelSize(16)
    font2.setWeight(QFont.Bold)
    splash2.setFont(font2)
    splash2.showMessage("Fetching\nLatest X64dbg",
                       QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom | QtCore.Qt.WindowStaysOnTopHint, QtCore.Qt.white)

    splash2.show()
    time.sleep(3)
    zfile_size_dl = 0
    zf = open(zfile_name, 'wb')
    zmeta = zu.info()
    zfile_size = int(zmeta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (zfile_name, zfile_size)

    zfile_size_dl = 0
    zblock_sz = 8192
    while True:
        zbuffer = zu.read(zblock_sz)
        if not zbuffer:
            break

        zfile_size_dl += len(zbuffer)
        zf.write(zbuffer)
        zstatus = r"%10d [%3.2f%%]" % (zfile_size_dl, zfile_size_dl * 100. / zfile_size)
        zstatus = zstatus + chr(8) * (len(zstatus) + 1)
        zfont = splash2.font()
        zfont.setPixelSize(16)
        zfont.setWeight(QFont.Bold)
        splash2.setFont(font2)

        splash2.showMessage("Downloading\n" + zreg2 + "\n" + zstatus,
                           QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom | QtCore.Qt.WindowStaysOnTopHint,
                           QtCore.Qt.white)
        splash2.show()

    PyQt5.QtWidgets.QApplication.processEvents()
    splash2.show()
    new_build_folder = os.getcwd()
    os.system("explorer " + new_build_folder)
    print dn

    splash2.finish(splash2)


def X64dbgSplashpy(self):
    splash = PyQt5.QtWidgets.QSplashScreen(QtGui.QPixmap("22.png"), QtCore.Qt.WindowStaysOnTopHint)
    font = splash.font()
    font.setPixelSize(16)
    font.setWeight(QFont.Bold)
    splash.setFont(font)

    splash.showMessage("Fetching\nLatest X64dbg python Build", QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom | QtCore.Qt.WindowStaysOnTopHint, QtCore.Qt.white)

    splash.show()
    time.sleep(3)
    file_size_dl = 0
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
             break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8) * (len(status) + 1)
        font = splash.font()
        font.setPixelSize(16)
        font.setWeight(QFont.Bold)
        splash.setFont(font)

        splash.showMessage("Downloading\n" + reg2+"\n"+status, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom | QtCore.Qt.WindowStaysOnTopHint, QtCore.Qt.white)
        splash.show()

    PyQt5.QtWidgets.QApplication.processEvents()
    splash.show()



    if splash.finish(splash) == True:
        return X64dbgSplash()
    else:
        print "wait"



if __name__ == '__main__':

    import sys
    app = PyQt5.QtWidgets.QApplication.instance() #enable for usage outside x64dbg
    if not app: #enable for usage outside x64dbg
        app = PyQt5.QtWidgets.QApplication([]) #enable for usage outside x64dbg

    X64dbgSplashpy(sys.argv)
    X64dbgSplash(sys.argv)

    app.exec_()



