import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 14, 16, 19, 22, 23, 25, 29, 33, 36, 38]
NEEDLES = [0, 1, 2, 4, 8, 13, 16, 17, 21, 28, 32, 39]

ROW_FMT = '{0:2d} @ {1:2d}     {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        pos = bisect_fn(HAYSTACK, needle)
        offset = pos * '  |'
        print(ROW_FMT.format(needle, pos, offset))

if __name__ == "__main__":

    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect
    
    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)
