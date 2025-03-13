import os
import shutil

from static_to_public import copy_files_recursive

dir_path_static = "./static"
dir_path_public = "./public"




def main():

    # Step 1: Load and execute `copy_files_recursive()`
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
        
    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    

main()
