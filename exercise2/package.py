"""
Script that will package our application to be delivered.
"""
import os, sys
import tarfile

def create_tar(tar_filename):
    """
    Function for checking if built artifact is present and tar it.
    """
    if os.path.exists("build/app.pyc"):
        with tarfile.open("package/{}.tar.gz".format(tar_filename), "w:gz") as tar:
            tar.add("build/app.pyc")
        tar.close()
        print("Done... Over and Out!")
    else:
        print("Compiled application wasn't found, please, build it before proceeding...")

def main(tar_filename):
    """
    Prepare the package directory and call the tar function.
    """
    print("Packaging our application...")
    if not os.path.exists("package/"):
        print("Creating missing 'package' directory...")
        os.mkdir("package/")
    else:
        print("Packaging directory exists, cleaning it up...")
        if os.path.exists("package/"):
            for root, dirs, files in os.walk("package/", topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))

    create_tar(tar_filename)

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Missing argument. Please, provide the package name, without the .tar.gz, just a word.")
    else:
        main(sys.argv[1])
