#!/usr/bin/env python
# -*- coding: gbk -*-


###########################################  
# File Name     : convert.py
# Author        : liqibo(liqibo@baidu.com)
# Created Time  : 2017/8/05
# Brief         : convert encode to another
###########################################


__revision__ = '0.1'
import sys



def convert_encoding(line, from_encode, to_encode):
    # convert encode
    line = line.decode(from_encode, "ignore")
    line = line.encode(to_encode, "ignore")
    return line

def run(from_encode, to_encode):

    for line in sys.stdin:
        line = convert_encoding(line, from_encode, to_encode)
        print line,

    return 0


def main(from_encode, to_encode):
    """
    statement
    """
    exit(run(from_encode, to_encode))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print >> sys.stderr, "error argv: python %s from_encode to_encode" % sys.argv[0]
        exit(1)
    main(sys.argv[1], sys.argv[2])







