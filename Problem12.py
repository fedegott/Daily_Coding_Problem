"""This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time."""

import random
from itertools import chain
N = 4
# brute force method
# random.seed(42)
# alist =[[]]
# for i in range(10):
#     k=0
#     alist.append([])
#     while k < N:
#         rand = random.randint(1, 2)
#         k += rand
#         if k < N:
#             alist[i].append(rand)


random.seed(42)

for i in range(10):
    alist = []
    alist1= []
    alist2 = set()
    k=0
    while k<N:
        rand = random.randint(1,2)
        k+= rand
        alist.append(rand)
        if k == N:
            alist1.append(alist)
            alist1.sort() # does not sort it
    # alist2.add(alist1)
    #alist1.sort() --> sorts alist1 and returs none while sorted(alist1) does not sort alist1 but create a new list that it's sorted
    # alist2 = set(sorted(map(tuple,sorted(alist1))))
    # alist2 = alist1.sort()
    print(alist1) # Can't get rid of the duplicates not order the set, so no point converting into a set, rather
