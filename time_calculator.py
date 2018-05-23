import timeit
import matplotlib.pyplot as plt
import numpy as np
import random

""" This is a program to be imported when need to compute the time it takes a function to run"""

from Problem9 import nonadjsum, alist

time = []
def time_calculation1(func, list,num_cycles): # input are the functions ( which should return a list), the list (which is the input of the function) and the number of numbers that want to add to the argument list
    random.seed(0)
    for i in range(num_cycles):
        list.append(random.randint(0,100))
        starttime = timeit.default_timer()
        func(list)
        t = timeit.default_timer() - starttime
        time.append(np.average(t))
    return time

################# TEST ######################

result1 = time_calculation1(nonadjsum,alist,50)