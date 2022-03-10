#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with open("file2.txt", "r") as fileptr:
        print("The filepointer is at byte : ", fileptr.tell())
        content = fileptr.read()
        print("After reading, the filepointer is at:", fileptr.tell())

