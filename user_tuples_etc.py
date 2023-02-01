"""
Trevor Arellanes
Data Analytics Fundamentals
1.31.23
"""
print("tuples")
# create some tuples
print("created tuples are:")
team1 = ("Derrick", "Connor", "St. Mary,")
team2 = ("Dale", "Richard", "University of Kansas")
print()
#tuple repetition
print("demonstration of tuple repetition.")
team1_trip = team1 * 3
print(team1_trip)
print("demonstration of tuple concatenation")
print()
#tuple concetanation
team2cat = team2 + team1
print(team2cat)
print()
print("demonstration of syntactic sugar f string.")
#syntactic sugar f string
print(f"{team1 = }")
print(f"{team2 = }")

#=====================
# Sets
print()
print("Sets")
print()
#create 2 sets
test_score1 = {43, 47, 40, 50, 47, 49, 45}
test_score2 = {49, 46, 44, 48, 50, 50,}
#set union
test_score3 = test_score1 | test_score2

#set intersection
test_score3_all = test_score1 & test_score2
print(f"test_score 1 is: {test_score1}")
print(f'test_score 2 is: {test_score2}')
print()
print("the union of the two set results is: ")
print(f'{test_score3}')
print()
print("the intersection of the two sets will result in test scores scored on both test 1 and 2")
print(f'these score are: {test_score3_all}')
print()
#===========================================================================
# Dictionaries
print("Dictionaries")

with open("text_simple.txt") as file_object:
    wordlist = file_object.read().split()

wordlist_lower = [x.lower() for x in wordlist] # change to lowercase
wordlist_mod = [str.replace(",", "") for str in wordlist_lower] # remove ,
wordlist_mod2 = [str.replace("?", "") for str in wordlist_mod] # remove ?
wordlist_mod3 = [str.replace(".", "") for str in wordlist_mod2] # remove .

wordcounts_dict = {word: wordlist_mod3.count(word) for word in wordlist_mod3}

print()
print("Below is a created a dictionary of word : count for each word in the woodchuck text")

print(wordcounts_dict)