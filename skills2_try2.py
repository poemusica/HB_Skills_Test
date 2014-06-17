string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "San", "I", "am"]

### TEST NO. 1 ###
"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""
def count_unique(string1):
    d = {}
    for char in string1:
        d[char] = d.get(char, 0) + 1
    return d

# print count_unique(string1)



### TEST NO. 2 ###
"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists
"""
# This algorithm is sub n^2. Returns a sorted copy.
def sort_list(l):
    s =[ l[0] ]
    for e in l[1:]:
        for i in range(len(s)):
            if e <= s[i]:
                s.insert(i, e)
                break
            i += 1
        else:
            s.append(e)
    return s

print sort_list(list1)
print sort_list(list2)


def common_items(list1, list2):
    result = []
    s1 = sort_list(list1)
    s2 = sort_list(list2)
    s2_len = len(s2)
    i = 0

    for e in s1:
        while e > s2[i]:
            i += 1
            if i >= s2_len:
                return result
        if e == s2[i]:
            result.append(e)
            while e == s2[i]:
                i += 1
                if i >= s2_len:
                    return result
    return result

print common_items(list1, list2)
print common_items(list2, list1)






### TEST NO. 3 ###
"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""
def common_items2(list1, list2):
    pass



### TEST NO. 4 ###
"""
Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(list1):
    pass



### TEST NO. 5 ###
"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
    pass



### TEST NO. 6 ###
"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""
def word_length(words):
    pass



### TEST NO. 7 ###
"""
Here's a table of English to Pirate translations
English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey

Write a program that asks the user to type in a sentence and then
print the sentece translated to pirate.
"""