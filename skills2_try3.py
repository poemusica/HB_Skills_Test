string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "Sam", "I", "am"]


### TEST NO. 0 ###
"""Write a function that takes a string and returns a list of all unique elements in the string."""
def unique():
    results = []
    words = string1.split()
    for i in range(len(words)):
        if words[i] not in words[:i] and words[i] not in words[i+1:]:
            results.append(words[i])
    return results

str2 = "yes no no hooray this is awesome yes yes"
# print count_unique(str2)

### TEST NO. 1 ###
"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""
def count_unique(string1):
    results = {}
    words = string1.split()
    for w in words:
        results[w] = results.get(w, 0) + 1
    return results

# print count_unique(string1)
# print count_unique(str2)


### TEST NO. 2 ###
"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists
"""
def common_items(list1, list2):
    results = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                for k in range(len(results)):
                    if list1[i] == results[k]:
                        break
                else:
                    results.append(list1[i])
    return results

# print common_items(list1, list2)

### TEST NO. 3 ###
"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""
def common_items_dict(l1, l2):
    results = []
    d = {}
    for i in range(len(l1)):
        d[l1[i]] = d.get(l1[i], True)
    for i in range(len(l2)):
        if d.get(l2[i]):
            results.append(l2[i])
    return results

def common_items_dict2(l1, l2):
    results = []
    d = {}
    for i in range(len(l1)):
        d[l1[i]] = d.get(l1[i], 1)
    for i in range(len(l2)):
        d[l2[i]] = d.get(l2[i], 0) + 2
    for k in d:
        if d[k] > 1 and d[k] % 2:
            results.append(k)
    return results

# print common_items_dict([1, 2, 2, 3], [4, 5, 1, 3, 5])
# print common_items_dict2([1, 2, 2, 3], [4, 5, 1, 3, 5])


### TEST NO. 4 ###
"""
Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(l):
    results = []
    for i in range(len(l)):
        for j in range(len(l)):
                if i != j and l[i] + l[j] == 0:
                    for k in range(len(results)):
                        if results[k][0] == l[i] or results[k][1] == l[i]:
                            break
                    else:
                        results.append((l[i], l[j]))
    return results

def sum_zero_dict(l):
    results = []
    d = {}
    for i in range(len(l)):
        if -l[i] in d:
            d[l[i]] = True
            d[-l[i]] = True
        else:
            d[l[i]] = False
    for k in d:
        if d[k] and k > 0:
            results.append((k, -k))
    return results

def sum_zero_dict2(l):
    results = []
    d = {}
    for i in range(len(l)):
        if -l[i] in d:
            d[-l[i]] = True
        else:
            d[l[i]] = d.get(l[i], False)
    for k in d:
        if d[k]:
            results.append((k, -k))
    return results


def sum_zero_dict3(l):
    results = []
    d = {}
    for item in l:
        if d.get(-item):
            results.append((item, -item))
            del d[-item] # prevents same item from being paired with multiple opposites
        else: d[item] = True
    return results

print sum_zero_dict3(list1)
print sum_zero_dict3(list2)



### TEST NO. 5 ###
"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
    results = []
    for i in range(len(words)):
        if words[i] not in words[:i] and words[i] not in words[i+1:]:
            results.append(words[i])
    return results

# print find_duplicates(words)

def find_duplicates_dict(words):
    results = []
    d = {}
    for i in range(len(words)):
        d[words[i]] = d.get(words[i], 0) + 1
    for k in d:
        if d[k] < 2:
            results.append(k)
    return results

# print find_duplicates_dict(words)


### TEST NO. 6 ###
"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""

# non-alphabetical solution
def word_length(words):
    for countdown in range( len(words) - 1, 0, -1):
        for i in range(countdown):
            if len(words[i]) > len(words[i +1]):
                temp = words[i]
                words[i] = words[i+1]
                words[i+1] = temp
    return words

#print word_length(words)

# alphabetical solution: length scopes over alpha
def word_list2(words):
    pass


# alphabetical solution: alpha scopes over length
def word_list3(words):
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