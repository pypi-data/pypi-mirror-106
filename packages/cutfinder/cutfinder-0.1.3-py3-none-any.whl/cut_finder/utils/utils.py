#!/usr/bin/env python
"""
A new .py file

"""

__author__ = 'ccluff'


def parse_arg(arg: str):
    arg = arg.replace('[', '').replace(']', '').replace(' ', '').split(',')
    return list(map(float, arg))
