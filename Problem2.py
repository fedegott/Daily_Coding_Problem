"""Problem#2"""

""""Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6]."""


#--> commments
""" xx """ #--> Docstring (document string) all the comments insdide """ xxx """ can be accessed using function and EXPLAIN what the function does and what are the arguments. The doc string line should begin with a capital letter and end with a period.
# access the docstring by import the module in the python (shell) and doing help(my_function)
import copy


list_select = [5,10,15,20]
try1 = [1,2,3,4,5]
try2 = [3,2,1]
results = []

def multiply_except_selected(alist):
    results = [] # if don't do this to reinitizalize this list, then it uses the same results for each different list and on 3rd functions gives [3000,1500,1000,750,120,60,40,30,24,2,3,6]
    for i in range(len(alist)):
         alist1 = alist.copy() # --> if use alist1 = alist it does ALIASING, then when use alist.pop(0), alist will also loose that value. that's why I need to do a shallow copy, can't do assignemtn alist1 = alist
         # use alist.copy() for shallow copy, inserts REFERENCES into it to the objects found in the original, so if change original this will change. for deep copy use alist.deepcopy() which inserts COPIES into it of the objects found in the original
         result = 1
         alist1.pop(i)
         for j in alist1:
             result *= j
         results.append(result)
    # print(results)
    return results


a = multiply_except_selected(list_select)
print(a)

b = multiply_except_selected(try1)
print(b)

c = multiply_except_selected(try2)
print(c)