#!/usr/bin/env python3

# import additional code to complete our task
import shutil
import os

def main():
    # move into the working directory
    os.chdir("/home/student/mycode/")
    
    # copy the fileA to fileB
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
    
    # copy the entire directoryA to directoryB
    shutil.copytree("5g_research/", "5g_research_backup/")
    
    # The following line will create the directory if it does not exist already
    # checking if the directory demo_folder exist or not.
    # if the demo_folder directory is not present
    # then create it.
    if not os.path.exists("./demo_folder"):
        os.makedirs("demo_folder")

if __name__ == "__main__":
    main()
