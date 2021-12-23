#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def positive():
    print("Positive")


def negative():
    print("Negative")


def test():
    a = int(input("Put int num: "))
    if a > 0:
        positive()
    else:
        negative()


# def positive():
#     print("Positive")
#
#
# def negative():
#     print("Negative")


if __name__ == '__main__':
    test()
