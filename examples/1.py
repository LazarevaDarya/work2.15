#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    fileptr = open("file.txt", "r")
    if fileptr:
        print("file is opened successfully")
    fileptr.close()