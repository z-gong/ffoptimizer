#!/usr/bin/env python3
# coding=utf-8

import os
import sys
from optimizer import Optimizer

if __name__ == '__main__':
    optimizer = Optimizer(db_file='ffoptimizer.db')

    cmd = sys.argv[1]
    if cmd == 'init':
        optimizer.init_db(sys.argv[2])

    elif cmd == 'optimize':
        ppf_file = os.path.abspath(sys.argv[2])
        optimizer.optimize(ppf_file)

    elif cmd == 'npt':
        ppf_file = os.path.abspath(sys.argv[2])
        optimizer.npt(ppf_file)

    elif cmd == 'plot':
        ppfs = sys.argv[2:]
        optimizer.plot(ppfs, iteration=None)

    else:
        print('Unknown command')
