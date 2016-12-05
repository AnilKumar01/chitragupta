from os import path
from sofi import file_size_by_unit
from sys import argv
from time import strftime, gmtime


def last_mod_epoch_time(file_path):
    return gmtime(path.getmtime(file_path))


def last_mod_date_time(filePath, dateTime="%d/%m/%Y"):
    return strftime(dateTime, last_mod_epoch_time(filePath))


def file_mod_in_bytes(filePath, lastSizeOfFile=100):
    return abs(file_size_by_unit(filePath) - lastSizeOfFile)


if __name__ == '__main__':
    if len(argv) != 2:
        print("	Usage: filestat.py <filePath> ") 
        exit()
    print "Last File Mod Time: %s" %str(last_mod_date_time(argv[1], "%m/%d/%Y"))
    print "File Mod in Bytes: %s" %str(file_mod_in_bytes(argv[1]))
