#!/usr/bin/python3
import sys
if __name__ == '__main__':
    print(len(sys.argv),"argument(s)")
    for idx, arg in enumerate(sys.argv):
        print("{} : {}".format(idx, arg))
