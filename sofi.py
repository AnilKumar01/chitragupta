from os import stat
from sys import argv
from numpy import double

# this function will return the size of a file in bytes.
def file_size(file_name):
    tmp = stat(file_name)
    return tmp.st_size

# this function will return the size of a file in different units.
# e.g. B, KB, MB and GB
def file_size_by_unit(file_name, unit="b"):
    f_size = double(file_size(file_name))
    if unit == "k" or unit == "K":
        return round(f_size/1024.0, 4);
    elif unit == "m" or unit == "M":
        return round(f_size/1024.0/1024.0, 4);
    elif unit == "g" or unit == "G":
        return round(f_size/1024.0/1024.0/1024.0, 4);
    else:
        return f_size
        
        
if __name__ == '__main__':
    if len(argv) == 3:
        in_cmd = " ".join(argv)
        if "sofi.py -fk" in in_cmd or "sofi.py -kf" in in_cmd:
            print "%s KB" %str(file_size_by_unit(argv[2], "k"))
        elif "sofi.py -fm" in in_cmd or "sofi.py -mf" in in_cmd:
            print "%s MB" %str(file_size_by_unit(argv[2], "m"))
        elif "sofi.py -fg" in in_cmd or "sofi.py -gf" in in_cmd:
            print "%s GB" %str(file_size_by_unit(argv[2], "g"))
        elif "sofi.py -f" in in_cmd or "sofi.py -fb" in in_cmd or "sofi.py -bf" in in_cmd:
            print "%s B" %str(file_size_by_unit(argv[2]))
        else:
            pass
    else:
        pass