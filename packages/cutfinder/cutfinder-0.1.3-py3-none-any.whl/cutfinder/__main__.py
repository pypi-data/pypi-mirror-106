#!/usr/bin/env python
"""main"""

import sys

from cutfinder.cutfinder import CutFinder
from cutfinder.utils.utils import parse_arg


def main():
    """entry point for command line execution"""
    CutFinder(*map(parse_arg, sys.argv[1:]))


if __name__ == "__main__":
    main()
