# Wii-Menu-Patcher
A cross-platform tool for applying patches to the Wii System Menu, done by extracting and modifying the contents of the WAD, featuring a Qt6 GUI.

[![Python application](https://github.com/NinjaCheetah/Wii-Menu-Patcher/actions/workflows/python-build.yml/badge.svg)](https://github.com/NinjaCheetah/Wii-Menu-Patcher/actions/workflows/python-build.yml)

### System Requirements
**Windows:** 
- 8.1 or newer (required for Python > 3.9)
- Python 3.11

**Linux:** 
- A modern Linux distro that offers Python 3.11
- Python 3.11
- `Wine`, to run some required (currently) Windows-only tools

Python 3.12 is not fully compatible at this time. macOS is also unsupported at this time, because this tool relies on Windows exectuables that cannot easily be run on macos.

### Deployment
I use [Nuitka](https://github.com/Nuitka/Nuitka) to package Wii-Menu-Patcher for Windows and Linux without requiring any dependencies on the target computer.

To build it yourself, first install required Python modules with:
```
pip install -r requirements.txt
```
and then Nuitka to build the program for your platform:

**Windows:**
```
nuitka --assume-yes-for-downloads --standalone --plugin-enable=pyside6 main.py --disable-console
```

**Linux:**
```
nuitka3 --standalone --plugin-enable=pyside6 main.py
```

The resulting build will be in `main.dist`. On Windows, you'll have an executable named `main.exe`, and on Linux you'll have an executable named `main.bin`. All required libraries for the program are located inside the `main.dist` directory, so you can use it on a different system without installing any dependencies.
