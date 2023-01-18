#!/usr/bin/env python3

import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import time
import argparse
import pascals_tri
import numpy
import sys


# TODO: put this in a library somewhere.
def time_function(fcn, args_list, kwargs_list=None):
    ''' time a function fcn. it will be called for each element in args and kwargs as fcn(*args, **kwargs).
    rvalue is [time per invocation] in order.'''
    
    times = []
    assert kwargs_list is None or len(args_list) == len(kwargs_list)
    for i in range(len(args_list)):
        
        start = time.perf_counter() # do not use time.time() because that is often a syscall.
        
        fcn(*(args_list[i]), **(kwargs_list[i] if kwargs_list is not None else {}))

        end = time.perf_counter()

        times.append(end - start)
    return times


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--iterations", help="number of iterations", type=int, required=True)
    parser.add_argument("--step", help="step between iterations", type=int, default=1)
    parser.add_argument('--outfile', help='figure output filename', required=True)
    args = parser.parse_args()
    
    trials = range(1, args.iterations+1, args.step)
    args_list = [[x] for x in trials]
    
    times = time_function(pascals_tri.pascal, args_list)
    plt.scatter(x=trials, y=times)
    plt.xlabel("number of lines")
    plt.ylabel("time to print")
    bestfit = numpy.polyfit(range(0, args.iterations, args.step), times, 3)
    print('cubic coefficients: %s' % bestfit, file=sys.stderr)
    bestfit_poly = numpy.poly1d(bestfit) 
    plt.plot(trials, bestfit_poly(trials))
    plt.savefig(args.outfile)
