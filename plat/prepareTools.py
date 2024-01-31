import os
import sys
import urllib
import threading
from urllib.request import urlopen

from PySide6.QtCore import QThread


toolsReady = False


def downloadFile(url, filename):
    with urlopen(url) as r:
        with open(filename, "wb") as f:
            f.write(r.read())


def downloadFiles(files):
    for file in files:
        threading.Thread(target=downloadFile, args=(file[0], file[1])).start()


def getOS():
    return sys.platform.system()
