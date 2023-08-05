#!/usr/bin/env python
"""
A new .py file

"""

__author__ = 'ccluff'

from typing import List


def parse_arg(arg: str) -> List[float]:
    """for parsing cli args from str to python objects"""
    arg = arg.replace('[', '').replace(']', '').replace(' ', '').split(',')
    return list(map(float, arg))
