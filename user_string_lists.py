"""
Trevor Arellanes
Data Analytics Fundamentals
1.31.23
domain: healthcare
"""

# imports first
import random

# define list of names
list_nurses = ["Grant", "Frank",  "Hannah", "Maeve", "Melanie"]
# define room assignments
room_assign = [112, 115, 119, 122, 133, 144, 129]
# define emergency code color
code_color = ["violet", "yellow", "brown", "orange", "white"]
# define physiologic system
physio_system = ["neurological", "musculoskeletal", "cardiovascular,"]
# define if patient is a fall risk
fall_risk = ["yes, " "no"]

print('We created 5 lists related to healthcare, specifically nursing.')
print('They are:')
print(f'names: {list_nurses}')
print(f'room assignment: {room_assign}')
print(f'emergency code color: {code_color}')
print(f'physiological system: {physio_system}')
print(f'fall risk: {fall_risk}')
print()
# String list 1. Using PYthon Built-in Functions
print('Below we will look at using python buid in functions on the text strings')
# len()
print("let's look at the length of some of the lists")
print()
length_nurses = len(list_nurses)
print(f'The length of list_nurses: {length_nurses}')
print(f'room_assign: {len(room_assign)}')
print(f'room_assign: {len(code_color)}')
print()
# set()
print('Next we will look at using the set() function')
print("To find unique values in the room assign list we can make it a set.")
print(f"The set of room assign is: {set(room_assign)}")
print()
def merge (list1, list2):
    """Returns a list of tuples from merging two string lists."""
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return merged_list
("Here we have merged two lists to form a tuple. This example uses nurse names and room assign")
print(merge(list_nurses, room_assign))
print()
# zip
print('Next we examine merging nurses with physiological systems')
print(list(zip(list_nurses, physio_system)))
#============================================================
# string lists 2 - random choice
print('String Lists 2 - Random Choice')
print()
# random value using random.choice
def random_pick(list):
    """return random value from list"""
    return random.choice(list)

print('It appears that we are overstaffed today, which nurse should we call off?')
print(f'The random nurse to be called off is: {random_pick(list_nurses)}')
print()

# sentence generation
sentence = (
f"{random_pick(list_nurses)} who is assigned to room {random_pick(room_assign)}"
f" and is knowledgeable in {random_pick(physio_system)} conditions had to call in a code {random_pick(code_color)}.")
print("Below is a random generated sentence using 3 lists from above.")
print(sentence)
#============================================================================================
# String List 3. Get Unique Words
print('String List 3. Get Unique Words')
print()
# read in Hamlet
with open("text_woodchuck.txt", "r") as fileObject:
    text = fileObject.read()
    list_words = text.split()  # split on whitespace
    unique_words = set(list_words)  # remove duplicates







