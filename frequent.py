W = input('Please enter a string ')
from collections import Counter
from heapq import nlargest

def ordered_letters(s, n=len(W)):
    ctr = Counter(c.lower() for c in s if c.isalpha())

    def sort_key(x):
        return (x[1], -ord(x[0]))

    for idx, (letter, count) in enumerate(nlargest(n, ctr.items(), key=sort_key), 1):
        print('#', idx, 'Most frequent:', letter, '.', 'Appearances:', count)

print(ordered_letters(W))
