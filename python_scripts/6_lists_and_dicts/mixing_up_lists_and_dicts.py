# In our initial examples, we had lists where all the items were the same

courseList = [ "315p", "225m", "345p" ]

# All the items in the list are strings.  But it doesn't have to be that way:

bagOfStuff = [ "hat", 7, 8, "tree", False, 9.7 ]

# We can also make up complex data structures by putting lists or dicts into lists
# or dicts.

letters = ["a","b","c"]
days = ["mon","tues","wed"]

listOfLists = [ letters , days ]

jamesCourses = { "101c": "Intoductory Zoology",
	              "210s": "Zoology Lab",
	             "315p": "Penguin Studies" }
	             
sarahCourses = { "890": "Dissertation Continuing",
	              "210s": "Zoology Lab",
	             "315p": "Penguin Studies" }

adviseesCourses = [ jamesCourses, sarahCourses ] 

# When you have complex data structures like these it can be hard to vizualise
# what is going on in them.  Thankfully python makes available a function called
# "pretty print" which is very handy.  It's not built in to the python language
# but it is supplied in a separate library of code that developers have made available
# Libraries are often called packages in python.

# That means that it has to be installed separately from python, which I've done on 
# holden. We also have to tell python to make that code available with an import call.
# If you don't have the import call you'll see: NameError: name 'pprint' is not defined

import pprint

# Now we can call the pprint.pprint() function (Yes, you have to type it twice
# separated by a period.  That's because it is the pprint function from the pprint
# library/package. 

pprint.pprint(adviseesCourses)
	             
