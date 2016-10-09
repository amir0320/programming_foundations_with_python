import os
def rename_files():
    file_list = os.listdir("/Users/Amir0320/Downloads/prank")
    os.chdir("/Users/Amir0320/Downloads/prank")
    for file_name in file_list:
        print "Old name is: " + file_name
        os.rename(file_name, file_name.translate(None, "0123456789"))
        print "New name is: " + file_name.translate(None, "0123456789")
rename_files()
