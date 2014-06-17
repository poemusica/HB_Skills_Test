# Things you should be able to do.

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    return [n for n in some_list if n % 2]

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    return [n for n in some_list if not n % 2]

# Write a function that takes a list of strings and returns a new list with all strings of length 4 or greater.
def long_words(word_list):
    return [w for w in word_list if len(w) > 4]

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    #return min(some_list)
    winner = some_list[0]
    for n in some_list:
        if n < winner:
            winner = n
    return winner

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    #return max(some_list)
    winner = some_list[0]
    for n in some_list:
        if n > winner:
            winner = n
    return winner

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    return [n/2.0 for n in some_list ]

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    return [len(w) for w in word_list]

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    #sum(numbers)
    result = 0
    for n in numbers:
        result += n
    return result

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    result = 1
    for n in numbers:
        result = result * n
    return result

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    result = ""
    for s in string_list:
        result += s
    return result

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    total = sum_numbers(numbers)
    ave = total / len(numbers)
    return ave