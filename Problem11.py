"""This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries."""

string_1 = 'de'
query_strings1 = ['dog', 'deer', 'deal']

string_2 = 'tor'
query_strings2 = ['tormentor','torpid', 'tortous', 'tory','toss', 'tomorrow', 'tuesday']

def autocomplete_system(string_, query_strings):
    result =[]
    for i in query_strings:
         if string_ == i[:len(string_)]: # this the most important part
             result.append(i)

    return result


print(autocomplete_system(string_1,query_strings1))
print(autocomplete_system(string_2,query_strings2))