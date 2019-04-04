# One thing that we do with List and Dicts is go through item by item and do
# things with them.  That way we can write a short piece of code and have it
# work on each item. In programming this is called "iterating", which means to
# do something over and over. Eventually we'll use this to process csv files
# and the results of SQL queries.

courseList = ["Introductory Zoology", "Zoology Lab", "Penguin Studies"]

# We can use a while loop with a counter to go through the List.
currIndex = 0
while(currIndex < len(courseList)):
    print("Processing item number {}".format(currIndex))
    # you use the currIndex as the index for accessing the right item in courseList
    currItem = courseList[currIndex]

    print("You are enrolled in " + currItem)

    # Now we increase the currIndex for the next go
    currIndex = currIndex + 1

# But there's also a short cut, called for (or "for each")
for currItem in courseList:
    print("You are enrolled in " + currItem)

# That's it, that's all that's needed; it works as the while does in the background
# but is much shorter.  Only downside is that you don't get the index number (but
# if you need that you can put a counter in the for, like this:

counter = 0
for currItem in courseList:
    print("You are enrolled in " + currItem)
    counter = counter + 1


# We can also iterate over Dicts.  Here we have to think about what we're
# iterating over. The easiest thing to get is each of the keys, and then use
# the key to get the value (just like you did with the index above).

courseDict = { "101c": "Intoductory Zoology",
	           "210s": "Zoology Lab",
	           "315p": "Penguin Studies" }

for courseNum in courseDict:
    print("You are enrolled in " + courseDict[courseNum])

# You can also get both the key and the value for each pair in a Dict,
# using Dict.items()  (Note that this is a python3 thing, if you see iteritems()
# then you are looking at someone talking about python2)
for courseNum, courseName in courseDict.items():
    print("Course " + courseNum + " is called " + courseName)

# I'm only using printing the items as an example, there are lots of other
# things you can do as you iterate through the List or Dict.  For example, you
# can add things up.

costs = [10,12,44,56,34,20]

total = 0
for cost in costs:
    total = total + cost

print(total)

# Or you can put together a sentence.
cities = ["London", "Paris", "Amsterdam", "Chennai"]

sentence = "The plane stopped at "
for city in cities:
    sentence = sentence + city + ", and then "

print(sentence + "finally we made it home.")

# Going through a list or a dict item by item and doing something is called "Iterating"
# which basically means repeat https://en.wiktionary.org/wiki/iterate

###########
# Sorting
##########

# Note that a List is its own order, but we can re-order it and then use that order
# that's called "sorting".  The easiest thing to sort by is alphabetical order
# note that numbers can also be sorted this way (alphabetical plus numbers is called
# "lexical" order.

# As Information School students we know that keeping the "original order"
# is sometimes very important!
mySortedList = sorted(courseList, reverse = True) # that creates a new list, leaving the original list

for currItem in mySortedList:
    print("You are enrolled in " + currItem)

# but if you don't care about the original order you can use:
courseList.sort() # this sorts the list "in place", changing the order

for myCourse in courseList:
    print("You are enrolled in " + myCourse)

#########
# Sorting a dict
#########

# You can sort a dict by the ordering of its keys using sorted.

courseDict = { "101c": "Intoductory Zoology",
	           "210s": "Zoology Lab",
	           "315p": "Penguin Studies" }

for key in sorted(courseDict):
    print("You are enrolled in " + courseDict[key])

###########
# Using items in a list to choose items from a Dict to output
###########

# We can always get the value of an item in a Dict if we have a string that
# matches its key.

states = { "TX": "Texas",
           "MD": "Maryland",
           "CA": "California",
           "NM": "New Mexico" }

# We can get the full name for California with:

print(states["CA"])

# if we have a List of state codes, we can iterate through that and lookup
# the full names of states.  So we can get things from the dict even when
# we aren't iterating through it.
two_states = ["CA", "TX"]

for state_code in two_states:
    print( states[state_code] )

# This can be really useful if you have a list (which has order) and you want to
# output a dict in the order of the list (maybe you've sorted it, or maybe it's in
# original order. You iterate through the list, using the items from the list as
# keys into the dict. (Note that you aren't iterating through the dict).
