# One thing that we do with List and Dicts is go through item by item and do things with
# them.  That way we can write a short piece of code and have it work on each item.
# Eventually we'll use this to process csv files and the results of SQL queries.

courseList = ["Introductory Zoology", "Zoology Lab", "Penguin Studies"]

for currItem in courseList:
    print("You are enrolled in a {} course".format(currItem))







# We can use a while loop with a counter to go through the List.
currIndex = 0
numItems = len(courseList) # gets the number of items in the List.
#numItems = 4

while(currIndex < numItems):
    print("Processing item number {}".format(currIndex))
    # you use the currIndex as the index for accessing the right item in courseList
    currItem = courseList[currIndex]

    print("You are enrolled in " + currItem)

    # Now we increase the currIndex
    currIndex = currIndex + 1
    # And cycle around the while loop again.


# But if we don't need the index then we don't have to do it that way.
# And this form is a lot simpler!

for course in courseList:
    print("You are enrolled in " + course)

# Note that the variable currItem is not a special word, it's just a variable
# name, so you can use anything.  Use something that makes sense to you.

# for myCourse in courseList:
#     print("You are enrolled in " + myCourse)

# We can access items in the list using an index.  These start at 0, funnily enough.
print(courseList[0])
print(courseList[1])
print(courseList[2])
# print(courseList[3]) going beyond the end gives a syntax error.


# Going through a list or a dict item by item and doing something is called "Iterating"
# which basically means repeat https://en.wiktionary.org/wiki/iterate

# Note that a List is its own order, but we can re-order it and then use that order
# that's called "sorting".  The easiest thing to sort by is alphabetical order
# note that numbers can also be sorted this way (alphabetical plus numbers is called
# "lexical" order.

# As Information School students we know that keeping the "original order"
# is sometimes very important!
mySortedList = sorted(courseList) # that creates a new list, leaving the original list

for currItem in mySortedList:
    print("You are enrolled in " + currItem)
#
# # but if you don't care about the original order you can use:
# courseList.sort() # this sorts the list "in place", changing the order
#
# for myCourse in courseList:
#     print("You are enrolled in " + myCourse)

# We can use a while loop with a counter to go through the List.
currIndex = 0
numItems = len(courseList) # gets the number of items in the List.

while(currIndex < len(courseList)):
    print("Processing item number {}".format(currIndex))
    # you use the currIndex as the index for accessing the right item in courseList
    currItem = courseList[currIndex]

    print("You are enrolled in " + currItem)

    # Now we increase the currIndex
    currIndex = currIndex + 1
    # And cycle around the while loop again.


# But if we don't need the index then we don't have to do it that way.
# And this form is a lot simpler!


# I'm only using printing the items as an example, there are lots of other
# things you can do as you iterate through the List or Dict.  For example, you
# can add things up.

costs = [10,12,44,56,34,20]

total = 0
for cost in costs:
    total = total + cost

print(total)



##########################
# Iterating on a Dict
#############################

# For Dicts we can go through them in two different ways.
# We can ask for the keys as a list, then iterate through them as a list
# and use them to get the items (just like using the currIndex number above).

courseDict = { "101c": "Intoductory Zoology",
	             "210s": "Zoology Lab",
	             "315p": "Penguin Studies" }

# Print "Penguin Studies"
print(courseDict["315p"]) ==>  "Penguin Studies"

courseDict["385T"] = "Data Wrangling"

# Iterate over items in the dictionary

for myKey in courseDict:
     currCourseNumber = myKey  # e.g., 101c
     currCourseName = courseDict[myKey]  # courseDict["101c"]
#
     print("You are enrolled in {}, named {}".format(currCourseNumber, currCourseName))

stateDictionary = { "TX": "Texas",
                    "AL": "Alabama",
                    "ND": "North Dakota",
                    "SD": "South Dakota" }

print(stateDictionary["SD"])

states_to_print = [ "TX", "ND" ]

# write a for loop to print "TX" and "ND"
for state in states_to_print:
  print(state) # "TX"


# change that loop to print out the full state names
for state in states_to_print:
  print(stateDictionary[state]) # Texas




# Here you are getting the keys as a list and then using them to access the values.
# If you happen to have a list from elsewhere that has the same types of things as the
# keys, then you could use that.  For example, you could get a list of abbreviations for
# the states that you have visited and iterate through those, using them as keys to
# a dict that has all the states.
#
# # Or we can either ask for each key-value pair (btw, this is something
# # that changed in python3, so remember to type python3 when googling.
#
# for currCourseNumber, currCourseName in courseDict.iteritems():
#     print("You are enrolled in {}, named {}".format(currCourseNumber, currCourseName))
#
# # this is often written as for key, value in myDict but just as with currItem above
# # there's nothing special about key and value there, those are just temp variable
# # names to receive each item as we iterate.
