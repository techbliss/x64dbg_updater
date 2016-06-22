import PyQt4
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QFont, QPixmap, QSplashScreen
import os
import sys
import time
import urllib2
import json
import webbrowser as pizzaheaven


dn = os.getcwd()
os.chdir(dn)

req = urllib2.Request("https://api.github.com/repos/x64dbg/x64dbg/releases/latest")
opener = urllib2.build_opener()
f = opener.open(req)
json = json.loads(f.read())
#print json debug only
branch = json[u'name']
first_up = "https://github.com/x64dbg/x64dbg/releases/download/snapshot/"
reg2 = first_up + branch
build_date = reg2
file_name = reg2.split('/')[-1]
u = urllib2.urlopen(reg2)

def X64dbgSplash(self):
    splash = QtGui.QSplashScreen(QtGui.QPixmap("22.png"))
    #splash.showMessage("Downloading:" % (reg2), QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.white)
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
        splash.showMessage(status, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom | QtCore.Qt.WindowStaysOnTopHint, QtCore.Qt.white)
        splash.show()

    QtGui.QApplication.processEvents()
    splash.show()
    new_build_folder = os.getcwd()
    pizzaheaven.open(new_build_folder)

    splash.finish(splash)

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    X64dbgSplash(([0]))
    app.quit()