"""
This script will compile/build our application exercise2.py
"""
import py_compile
import os
def build():
    """
    Function that will be used to build our application.
    """
    print("\033[1;33;40mCompiling our application...\033[0m")
    py_compile.compile("exercise2.py", "build/app.pyc")
    print("\033[1;32;40mDone... Application can be found in build/ directory\033[0m")

def check_dir():
    """
    Function that will be used to check if build directory exists, if not, create it then call build function.
    """
    buil_dir="build/"
    if not os.path.exists(buil_dir):
        print("\033[1;33;40mCreating build directory...\033[0m")
        try:
            os.mkdir(buil_dir)
            print("\033[1;32;40mBuild directory created...\033[0m")
        except Exception as error:
            raise Exception("Error creating build directory at: {}".format(buil_dir))
            print("\033[1;35;40mError creating dir: {}\033[0m".format(error))
            print()
        else:
            build()
    else:
        print("\033[1;33;40mBuild directory found... build to build now!\033[0m")
        build()

if __name__ == "__main__":
    check_dir()
