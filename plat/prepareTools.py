import os
import sys
import urllib
import threading


def getToolsIndex():
    currentOS = sys.platform.system()
    if currentOS == "Linux":
        return [
            ("https://github.com/mogzol/sharpii/releases/latest/download/Sharpii_v1.7.3.zip", "Sharpii.zip"),
            ("https://github.com/NinjaCheetah/ASH_Extractor/releases/latest/download/ASH-Linux.tar", "ASH-Linux.tar"),
            ("https://github.com/NinjaCheetah/ASH_Extractor/releases/latest/download/ashcompress.zip", "ashcompress.zip")
        ]
    elif currentOS == "Windows":
        return [
            ("https://github.com/mogzol/sharpii/releases/latest/download/Sharpii_v1.7.3.zip", "Sharpii.zip"),
            ("https://github.com/NinjaCheetah/ASH_Extractor/releases/latest/download/ASH-Windows.zip", "ASH-Windows.zip"),
            ("https://github.com/NinjaCheetah/ASH_Extractor/releases/latest/download/ashcompress.zip", "ashcompress.zip")
        ]
