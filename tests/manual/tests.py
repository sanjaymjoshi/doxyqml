#!/usr/bin/env python3

import platform
from subprocess import call

def main():
    doxyfileName = "Doxyfile"
    if platform.system() == "Windows":
        print ("Windows")
        doxyfileName = "Doxyfile.windows"

    call(["doxygen", doxyfileName])
    
    
if __name__ == "__main__":
    main()
# vi: ts=4 sw=4 et
