"""This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 8] should return 12, since we pick 4 and 8. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?"""

import timeit
import matplotlib.pyplot as plt
import numpy as np
import random

alist = [2,4,6,8]



def nonadjsum(list):
    temp = 0
    counter = 0
    for i in range(len(list)-2):
        if  alist[i]+list[i+1] > temp:
            temp = list[i]+list[i+1]
            counter += 1
            # print("talk to me %s %s" %(temp, counter)) ¢---> this is how use prting with %s and 2 strings
            # print(temp)
    return temp

nonadjsum(alist)

# t = timeit.Timer('nonadjsum([2,4,6,8,10,2,10,12,2,3,4,12,3])', setup="from __main__ import nonadjsum").timeit(number=100)
# t = timeit.Timer('nonadjsum([2,4,6,8])', setup="from __main__ import nonadjsum").repeat(repeat=10,number=10)
# time = np.average(t)

randint = np.random.randn(1)

# def list_creation(list, num_cycles):
#
#     random.seed(0)
#     for i in range(num_cycles):
#         list.append(random.randint(0,100))
#     return list

# time = []
# def time_calculation(list):
#     starttime = timeit.default_timer()
#
#     nonadjsum(list)
#     t = timeit.default_timer() - starttime
#     time.append(np.average(t))
#     return time

time = []
def time_calculation(list,num_cycles):
    random.seed(0)
    for i in range(num_cycles):
        list.append(random.randint(0,100))
        starttime = timeit.default_timer()
        nonadjsum(list)
        t = timeit.default_timer() - starttime
        time.append(np.average(t))
    return time





# print(nonadjsum(alist))
# print(list_creation(alist,5))

result = time_calculation(alist,100)
print(result)


plt.plot(result)
plt.ylabel('time in seconds')
plt.xlabel('list size')
plt.show()