#!/usr/bin/env python3
# -*- coding: utf-8 -*-

PI = 3.14


def circle(r):
    return PI * (r * r)


def cylinder():
    h = float(input("Put high of cylinder: "))
    r = float(input("Put radius of cylinder: "))
    x = int(input("1 - Calc only side area\n2 - Calc full area\n"))

    if x == 1:
        area = 2 * PI * r * h
    elif x == 2:
        area = 2 * PI * r * h
        area = 2 * (circle(r))
    print(area)


if __name__ == '__main__':
    cylinder()
