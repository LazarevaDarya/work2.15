#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os


if __name__ == "__main__":
    os.rename("alg.txt", "OPI.txt")
    with open("OPI.txt", "w",  encoding='utf-8') as fileptr:
        fileptr.write(
            "Отчет по лабораторной работе по дисциплине: \n"
            "Основы программной инженерии"
        )

