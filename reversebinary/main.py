#! /usr/bin/env python2.6
import sys
from reversebinary import ReverseBinary

if __name__=='__main__':
    reverseBinary = ReverseBinary();
    for line in sys.stdin:
        print reverseBinary.convert(line)
