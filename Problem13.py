"""This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb"."""


string_ = 'abcba'   # answer is dff
k = 2


# alist = []
# alist.append(string_[0])
# for i in range(len(string_)-1):
#
#     if string_[i] == string_[i+1]:
#         alist.append(string_[i+1])
#
#     elif string_[i] != string_[i+1]:
#
#         if len(alist) < k:
#             alist.append(string_[i+1])
# print(alist)

alist = []
alist.append(string_[0])
for i in range(len(string_)):
    string_[:i]