from ldir import list_dir_subdir
from sofi import file_size_by_unit
from sys import argv

# this function will give the size of a directory in specific units.
# i.e. B, KB, MB, and GB
def directory_size(dir_name, unit="b"):
    dir_contents = list_dir_subdir(dir_name)
    d_size = 0.0
    for item in dir_contents:
        d_size += file_size_by_unit(item, unit)
    return d_size
    
    
if __name__ == '__main__':
    if len(argv) == 3:
        in_cmd = " ".join(argv)
        if "sod.py -dk" in in_cmd or "sod.py -kd" in in_cmd:
            print "%s KB" %str(directory_size(argv[2], "k"))
        elif "sod.py -dm" in in_cmd or "sod.py -md" in in_cmd:
            print "%s MB" %str(directory_size(argv[2], "m"))
        elif "sod.py -dg" in in_cmd or "sod.py -gd" in in_cmd:
            print "%s GB" %str(directory_size(argv[2], "g"))
        elif "sod.py -d" in in_cmd or "sod.py -db" in in_cmd or "sod.py -bd" in in_cmd:
            print "%s B" %str(directory_size(argv[2]))
        else:
            pass
    else:
        pass
    