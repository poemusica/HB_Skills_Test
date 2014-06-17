string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7, 2]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "Sam", "I", "am"]


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

def count_unique_bonus():
    filename = 'twain.txt'
    f = open(filename)
    c = f.read()
    return count_unique(c)

# print count_unique_bonus()




### TEST NO. 2 ###
"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists.
for loop ok.
"""
def common_items_no_in(list1, list2):
    result = []
    l2_copy = list2[:]
    i = 0
    while i < len(list1):
        j = 0
        while j < len(l2_copy):
            if list1[i] == l2_copy[j]:
                result.append(l2_copy[j])
                l2_copy.remove(l2_copy[j])
                break
            j += 1
        i += 1

    return result

# print common_items_no_in(list1, list2)

def common_items(list1, list2):
    result = []
    l1_copy = list1[:]
    l2_copy = list2[:]
    for item1 in l1_copy:
        for item2 in l2_copy:
            if item1 == item2:
                result.append(item2)
                #l1_copy.remove(item1)
                l2_copy.remove(item2)
    return result

print common_items(list1, list2)



### TEST NO. 3 ###
"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""

def common_items2_no_in(list1, list2):
    d = {}
    result = []
    i = 0
    j = 0
    k = 0

    while i < len(list1):
        key = list1[i]
        value = d.get(key, None)
        if not value:
            d[key] = (True, False)
        i += 1

    while j < len(list2):
        key = list2[j]
        value = d.get(key, None)
        if not value:
            d[key] = (False, True)
        else:
            d[key] = (True, True)
        j += 1

    l = d.items()
    while k < len(l):
        item = l[k]
        if item[1] == (True, True):
            result.append(item[0])
        k += 1

    return result

# print common_items2_no_in(list1, list2)

def common_items2(list1, list2):
    d = {}
    result = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                key = item1
                d[key] = True
    for k in d:
        if d[k] == True:
            result.append(k)
    return result

# print common_items2(list1, list2)



### TEST NO. 4 ###
"""
Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(list1):
    d = {}
    mylist = list1[:]
    for n in mylist:
        for m in mylist:
            if (n + m) == 0:
                pair = (n, m)
                d[pair] = True
                mylist.remove(m)
    if d:
        return d.keys()
    return None

# print sum_zero(list1)
# print sum_zero(list2)



### TEST NO. 5 ###
"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
    result = words[:]
    i = 0
    while i < len(result):
        j = 0
        while j < len(result):
            w1 = result[i]
            w2 = result[j]
            if (i != j) and (w1 == w2):
                result.remove(w2)
            else:
                j += 1
        i += 1
    return result

# print find_duplicates(words)



### TEST NO. 6 ###
"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""

# first print all one letter words in alpha order. then print all two letter words in alpha order...

def ordered_insert(word, mylist):
    i = 0
    if mylist:
        while i < len(mylist):
            if word.lower() < mylist[i].lower():
                break
            i += 1
    mylist.insert(i, word)
    return mylist

def word_length(words):
    d = {}
    for w in words:
        length = len(w)
        d[length] = d.get(length, [])
        if w not in d[length]:
            d[length] = ordered_insert(w, d[length])
    for v in d.itervalues():
        for w in v:
            print w + ', ', 

# word_length(words)

# def shorter_and_alpha():


def word_length_no_in(words):
    first = words[0]
    l = [first]
    for w in words[1:]:
        if w not in l:
            i = 0 
            while i < len(l):
                len_w = len(w)
                len_i = len(l[i])
                if len_w < len_i:
                    l.insert(i, w)
                    break
                if len_w == len_i:
                    if w.lower() <= l[i].lower():
                        l.insert(i, w)
                        break
                    else:
                        i += 1
                else:
                    i += 1
        if w not in l:
            l.append(w)

    print ', '.join(l)

# word_length_no_in(words)




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

trans = {
'sir': 'matey',
'hotel': 'fleabag inn',
'student': 'swabbie',
'boy': 'matey',
'madam':'proud beauty',
'professor': 'foul blaggart',
'restaurant': 'galley',
'your': 'yer',
'excuse': 'arr',
'students': 'swabbies',
'are': 'be',
'lawyer': 'foul blaggart',
"the": "th'",
'restroom': 'head',
'my': 'me',
'hello': 'avast',
'is': 'be',
'man': 'matey'
}

def pirate(mydict):
    r = raw_input("English to Pirate Translator.\nInput your text here:\n")
    l = r.split()

    translation = []
    for w in l:
        t = mydict.get(w, w)
        translation.append(t)
    print " ".join(translation)

# pirate(trans)





