""" Problem 1"""

"""
Good morning! Here's your coding interview problem for today.

Given a list of numbers, return whether any two sums to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

"""

import timeit

def sum_a(alist, ak):
    for i in alist:
        blist = alist.copy()
        blist.remove(i)
        for j in blist:
            if i + j == ak:
                print("True", i,j)

    else: print("False")
    return

def sum_b(alist, ak):
    for i in range(len(alist)):
        j = i+1
        for j in range(len(alist)):
            print(alist[i],alist[j])
            if alist[i] + alist[j] == ak:
                print("True", alist[i],alist[j])

    else: print("False")
    return


k = 17
list = [10,5,3,7]

# t =timeit.Timer("sum_a([10,5,3,7],17)",setup = "from __main__ import sum_a").repeat(repeat = 5, number = 100)
# print(t)

starttime = timeit.default_timer() # 1st way to time it. simplets.
sum_a(list*100,k)
print(timeit.default_timer()-starttime)

# def j(a,b):
#     return print(a+b)

# # if __name__ == '__main__':


# # starttime = timeit.default_timer() # 1st way to time it. simplets.
# # j(3,4)
# # print(timeit.default_timer()-starttime)

# # t = timeit.timeit("j(2,3)",setup = "from __main__ import j", number = 100)  #https://stackoverflow.com/questions/8220801/how-to-use-timeit-module # 2nd way to time it
#The "from __main__ import ..." lets you use code from your main module inside the artificial environment created by timeit.

# # timeit.Timer(j(4,5)).timeit( number = 100)
# t = timeit.Timer("j(2,3)",setup = "from __main__ import j").repeat(repeat = 5, number = 100) # 3rd way to time it
# print(t)

for index, element in enumerate(list):
    print(index,element)

