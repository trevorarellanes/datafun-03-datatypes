"""
Trevor Arellanes
Data Analytics Fundamentals
1/28/23

"""

# import some modules first - how many can you make use of?

import math
import random
import statistics

# Task 3. Numeric Lists - Create lists (list1, listx, listy)
print("Task 3. Numeric Lists - Create lists (list1, listx, listy)")
print()
list1 = [114,
    25,
    321, 
    114,
    159,
    352,
    258,
    322,
    29,
    78,
    97,
    101,
    585,
    247,
    366,
    469,
    788,
    889,
    864,
    444]

listx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # time in minutes spent physician interacting with patients
    
listy = [100, 125, 145, 155, 140, 165, 200, 180, 225, 250] # patient satisfaction survey score
#=========================================================================================================
# Lists 2 - Correlation and Prediction
print("Lists 2 - Correlation and Prediction")
print()
print("We will let list1 represent number of bacteria in a sample from a patient in millions, and let listx represent time with patients spent by physician.")
print('Listy will represent the resulting patient satisfaction scores.')
print()
# define some functions
print('Below are some stastistical calculations to analyze the data given.')
print()
mean1 = statistics.mean(list1)
"""averages list1"""
print(f'The mean of list1 = {mean1}')

median1 = statistics.median(list1)
"""Finds median of list1"""
print(f'The median of list1 = {median1}')

mode1 = statistics.mode(list1)
"""Finds the mode of the list1"""
print(f'The mode of list1 is = {mode1}')
print()
stdev = statistics.stdev(list1)
"""provides standard deviation of list1"""
print(f'The standard deviation of list1 = {stdev:.2f}')

variance = statistics.variance(list1)
"""provides variance of list1"""
print(f'The variance of list1 = {variance:.2f}')

correlation = statistics.correlation(listx, listy)
"""Provides the correlation of listx and listy"""
print(f'The correlation of listx and listy = {correlation:.2f}')
print()
slope, intercept = statistics.linear_regression(listx, listy)
"""Provides the slope and intercept of the best line of fit for listx and listy"""
print(f'The slope intercept of listx and listy = {slope:.2f}, {intercept:.2f}')
print(f'The slope is = {slope:.2f}')
print(f'And the Y-intercept is = {intercept:.2f}')
print()
print("Let's try to predict some data next.")
future_value = 15 # from project 3 instruction
future_y = (slope * future_value + intercept) # predicted future y value from known information 
print()
print(f'Given the time with physicians of 15, the predicted patient satisfaction survey score is = {future_y:.2f}')
print('This makes sense as the general trend of the data is positive.')
print()
#======================================================================================================================
# Lists 3 - Using Python Built - in Functions
print("Lists 3 - Using Python Built - in Functions")
print()
# min and max scores and others
# return minimum 
minimum = min(list1)
# return maximum
maximum = max(list1)
# return number of values
number_bact = len(list1)
# return sum of values
sum_bact = sum(list1)
# return average of values
average_bact = sum_bact / number_bact
# return set of values
bact_set = set(list1)
# return sorted list ascending
asc_sort_bact = sorted(list1)
# return sorted list descending
des_sort_bact = sorted(list1, reverse=True)


print('Below are some Python Built-in Function results on the list1 data')

print(f'The lowest colony of bacteria: {minimum}')

print(f'The largest colony of bacteria: {maximum}')

print(f'Number of colonies of bacteria: {number_bact}')

print(f'Sum of bacteria: {sum_bact}')

print(f'Average bacteria: {average_bact}')

print(f'Set for bacteria: {bact_set}')

print(f'Bacteria sorted ascending: {asc_sort_bact}')

print(f'Bacteria sorted descending: {des_sort_bact}')
print()
#==============================================================================
#Lists 4 - List Methods
print('Lists 4 - List Methods')
print()
print('Below are a demonstration of using List Methods')
print()
print(f'Beginning with the original list: 55, 105, 225, 255.')
print(f'We can add 300 to the end of the list:')
lst = [55, 105, 225, 255]
print()

# Adding element to end of list
lst.append(300)
print(lst)
print()
# extend list with another list
print(f'Here we extend the list to add 1, 2, 3 at the end:')
lst.extend({1, 2, 3})
print(lst)
print()

# insert an item at a given position
print('Here we insert 525 into the list at the 3rd index of the list:')
i = 3
newvalue = 525
lst.insert(i, newvalue)
print(lst)
print()

# remove an item
print('Here we remove 525 from the list')
lst.remove(525)
print(lst)
print()

# Count how many times 2 appears in list
print('Here we count how many times "2" appears in the list:')
ct_2 = lst.count(2) 
print(ct_2)
print()

# Sort list ascending
print('Here we sort the list in ascending order:')
asc_score = lst.sort()
print(lst)
print()

# Sort list in descending order 
print('Here we sort the list in descending order:')
desc_score = lst.sort(reverse=True)
print(lst)
print() 

# copy the list to a new list
print('Below we copy lst to a newlst:')
newlst = lst.copy()
print(newlst)
print() 

# pop first item off the top of list
print('Here we take our new list and remove the first number of the list:')
first_pop = newlst.pop(0)
print(f'The old list: {lst} has {first_pop} removed from it')
print(f'leaving the current list: {newlst}')
print()

# pop last item off of list
print('Below we remove the last number from the list:')
last_pop = newlst.pop(-1)
print(f'The previous list has {last_pop} removed leaving: {newlst}')
print()
#=====================================
# Lists 5. List transformations filter() and map()
print("List 5 - List transformations using filter and map functions")
# Use filter() to only include numbers below 100
def get_below100(number):
    return number < 100
below100 = list(filter(get_below100, lst))
print()
print("Let's isolate the previous list to numbers below 100:")
print(below100)
print()

# Use map to map each number to it's square root
sq_root_num = list(map(lambda number: round(math.sqrt(number), 2), below100))
print('Next, we will show each of the remaining numbers from the previous list square rooted:')
print(sq_root_num)
print()
cube_of_2 = list(map(lambda number: number **3, filter (lambda number: number == 2, newlst)))
print(f'Now we will use the map function to find the volume of a cube using the number 2 from our list')
print(f'Since there is only 1 occurence of 2 in our list, the result is: {cube_of_2}')
print(cube_of_2)
print()
# List 6 - List Transformations - Using List Comprehension
print('List 6 - List Transformations - Using List Comprehension')
print()
print('Below we will find the numbers above 105 using list comprehension.')
above_105 = [number for number in lst if number > 105]
print('The result is listed below:')
print(above_105)
print()
print('Below we will triple each number in lst:')
tripled_score = [number * 3 for number in lst]
print(tripled_score)
print()
print('Next I will transform the data by subtracting 10 from each number:')
subtracted_10 = [number - 10 for number in lst]
print('The result is:')
print(subtracted_10)
print()

"""




# define more functions here (see instuctions)


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"


    # call your functions here (see instructions)
  


# Why? Why only print if this the module called?
# Because when you write good functions, you may want to
# import this module into another script - just like you did
# math or statistics.
# Build a library of resuable functions to support your domain.

# For example, if your domain:
# Is sports, create functions to provide a list of teams.
# Is pets, create functions to calculate adoption prices.
# Is music, create functions to return a list of your favorite artists.


# When you write reusable functions for your domain, you can
# import the module with your utility functions into other modules
# and use them there.  This is a very common practice.
# Anything you write can be imported into later projects.

"""