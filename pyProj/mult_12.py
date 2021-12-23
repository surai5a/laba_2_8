#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def mult():
    x = 1
    while True:
        a = int(input("Put numbers you want mult(0 - stop): "))
        if a == 0:
            break
        else:
            x = x * a
    if x == 1:
        exit()
    else:
        print(x)


if __name__ == '__main__':
    mult()
