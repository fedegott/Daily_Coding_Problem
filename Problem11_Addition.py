"""This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries."""

""" My problem is to retrieve all words beginning with a given query such as 'tor' from https://www.merriam-webster.com/browse/thesaurus/, webscraping the website"""

import urllib3
from bs4 import BeautifulSoup


url = 'https://www.merriam-webster.com/browse/thesaurus/'
query = 'de'

######## FIND NUMBER OF PAGES for the letter ########

def find_query(query,url):

    url_final = url + query[0]

    http = urllib3.PoolManager()
    web = http.request('GET',url_final)

    soup = BeautifulSoup(web.data, parse_only='html.parser') # do command+P ton see the arguments for any function!!!
    data = soup.find('span', attrs={'class':'counters'})

    pages = int((data.text[-2:])) # to simplify the code I assume that it will only have up to 99 pages for a given letter


########### get list of words starting with query[0]

    entries_total = []
    for i in range(pages+1):
        web_page = http.request('GET', url_final+'/'+str(i))
        soup_ = BeautifulSoup(web_page.data, parse_only='html.parser')
        entries = soup_.find('div', attrs={'class':'entries'})
        if i >0:
            entries_total.append(str(entries.text).split()) # this generates a list of list with all the words. entries_total[1][3] the index 1 is the page number of index3 is the 3rd word in that page

# print(entries_total[3][8])
# for j in range(len(entries_total):
#     for k in j:
#         print( query == entries_total)


# word = [[ i for i in k] for k in entries_total] # this is list comprehension to loop over list of lists
    results=[]
    for j in entries_total:

        for k in j:

            if query ==k[:len(query)]:
                results.append(k)

    return results

query1 = 'pop'
url1 = url

answer = find_query(query1, url1)
print(answer)




# print(shape(entries_total))# shape attribute is only for numpy, not for lists


