#!/usr/bin/env python
"""main"""

import sys

from cut_finder.cutfinder import CutFinder


def _parse_arg(arg: str):
    arg = arg.replace('[', '').replace(']', '').replace(' ', '').split(',')
    return list(map(float, arg))


def main():
    """entry point for command line execution"""
    CutFinder(*map(_parse_arg, sys.argv[1:]))


if __name__ == '__main__':
    main()