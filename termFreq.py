#! /usr/bin/env python

import sys
import collections

def main():
    filename = sys.argv[1]
    terms_count = collections.Counter()
    with open(filename, 'r') as f:
        n = int(next(f))
        for i in range(0, n):
            terms_count[next(f).strip()] += 1
        k = int(next(f))
    most_freq = terms_count.most_common(k)
    most_freq = sorted(most_freq, key = lambda x: (-x[1], x[0]))
    for term in most_freq:
        print term[0]

if __name__ == '__main__':
    main()