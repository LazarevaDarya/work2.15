#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with open("file2.txt", "r") as fileptr:
        for i in fileptr:
            print(i)
