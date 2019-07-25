"""
Script to clean our environment.
"""
import os

def main():
    print("Cleaning up the directories...")
    for folder in ["build/", "test/", "package/"]:
        if os.path.exists(folder):
            for root, dirs, files in os.walk(folder, topdown=False):
                for name in files:
                    print("Removing '{}'".format(os.path.join(root, name)))
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    print("Removing '{}'".format(os.path.join(root, name)))
                    os.rmdir(os.path.join(root, name))
            print("Removing '{}'".format(folder))
            os.rmdir(folder)
        else:
            print("No folder '{}' was found...".format(folder))
            
    print("Over and out!")

if __name__ == "__main__":
    main()
