#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
import os


with open('idz1.txt', encoding='utf-8') as file:
    for line in file.read().split('\n'):
        if line.strip().startswith('-'):
            print(line)
