from os import path, listdir
from sys import argv

# this function will return the content of the root directory with "/" prefix
# i.e. /xxx_content
def list_root_dir():
    root_contents = listdir("/")
    tmp = []
    for item in root_contents:
        tmp.append("/"+item)
    return tmp

# this function will return the content of a sub-directory with prefix of
# parent directory i.e. parent_dir/sub_dir/xxx_conetnt
def list_sub_dir(supdir, subdir):
    sub_directories_contents = listdir(supdir+"/"+subdir)
    tmp = []
    for item in sub_directories_contents:
        item = subdir + "/" +item
        tmp.append(item)
    return tmp

# this function will return the list of file in a directory including
# sub-directory files.
def list_dir_subdir(start_path):
    processing_stack = []
    if start_path == "/":
        processing_stack = list_root_dir()
    else:
        processing_stack = listdir(start_path);
    processed_stack =[];
    for item in processing_stack:
        tmp = start_path+"/"+item        
        if path.isdir(tmp):
            processing_stack.extend(list_sub_dir(start_path, item))
        else:
            processed_stack.append(tmp)
    return processed_stack

# function which will give the number of files in a directory (including sub-directories)
# to call this function use below command
# ldir.py -c directory
def get_file_count(dir_path):
    print len(list_dir_subdir(dir_path))
    
# function which will list all files in the given directory
# to call this function use below command
# ldir.py -a directory    
def list_all_files(dir_path):
    for item in list_dir_subdir(dir_path):
        print item

if __name__ == '__main__':
    if len(argv) == 3:
        in_cmd = " ".join(argv)
        if "ldir.py -c" in in_cmd:
            get_file_count(argv[2])
        elif "ldir.py -a" in in_cmd:
            list_all_files(argv[2])
        else:
            pass 
    else:
        pass
    