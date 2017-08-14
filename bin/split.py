#!/usr/bin/env python
# -*- coding: gbk -*-


###########################################  
# File Name     : split.py
# Author        : liqibo(liqibo@baidu.com)
# Created Time  : 2017/7/10
# Brief         : split file into num part
###########################################


__revision__ = '0.1'
import sys


def run(path_file, split_num):

    list_file_part = []
    dict_file_data = {}
    for i in range(0, split_num):
        list_file_part.append(path_file + "_part" + str(i))

    idx = 0
    with open(path_file) as file:
        for line in file:
            line = line.strip()
            file_name = list_file_part[idx]
            if file_name not in dict_file_data:
                dict_file_data[file_name] = []
            dict_file_data[file_name].append(line)
            idx = (idx + 1) % split_num

    for file_name in list_file_part:
        with open(file_name, 'w') as file:
            file.write("\n".join(dict_file_data[file_name]))

    return 0


def main(path_file, split_num):
    """
    statement
    """
    exit(run(path_file, split_num))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print >> sys.stderr, "%s path_file split_num" % sys.argv[0]
        exit(1)
    main(sys.argv[1], int(sys.argv[2]))




