#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_input():
    a = input("Put some string: ")
    return a


def test_input(a):
    return a.isnumeric()


def str_to_int(a):
    return int(a)


def print_int(a):
    print(a)


if __name__ == '__main__':
    x = get_input()
    if test_input(x) == 1:
        x = str_to_int(x)
        print_int(x)
