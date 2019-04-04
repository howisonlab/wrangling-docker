
# Teaching dicts.
#
# people and their ages.

names = ["bob","john","wei"]
ages = [32,33,45]

for index,name in enumerate(names):
    print("Person: {} is {} years old".format(name, ages[index]))

# dicts have keys and values
people = { "bob": 32,
           "john": 33,
           "wei": 34 }

for name in people: # iterates via keys, but the order is undefined.
    print("Person: {} is {} years old".format(name, people[name]))

# add a person and their age.
# List
# names.append("kangning")
# ages.append(28)
people["kangning"] = 28

# or
people.update( { "kangning": 28 })

# Same syntax for updating. Note that keys are unique
# This changes the value for the key "wei"
# There can only be a single "wei"
people["wei"] = 54

# Deleting items
del people["bob"]

#removed_value = people.pop("bob")

#handle trying to remove a key that isn't present
people.pop("bob", None)


# or people.pop("bob") which returns the value and can take a second argument to handle the situation if there is no key "bob", usually written as people.pop("bob", None)

# dicts values can themselves be dicts, a useful way to build a mini in-meory
# noSQL style database.
people = { "bob": { "age": 32, "hometown": "Austin"},
           "john": { "age": 33, "hometown": "Dallas" },
           "wei": {"age": 34, "hometown": "Shanghai" } }

for name in people: # iterates via keys
    person = people[name] # person is itself a dictionary
    template = "Person: {} is {} years old and comes from {}"
    print(template.format(name, person["age"], person["hometown"]))

# You can also iterate through the items in a dictionary
# getting keys and values.
for name, details in people.iteritems(): # iterates via keys
    template = "Person: {} is {} years old and comes from {}"
    print(template.format(name, details["age"], details["hometown"]))

# Sorting a dictionary.  Dictionaries have no order, but we can impose
# it by sorting the keys.
for name in sorted(people): # same as sorted(people.keys())
    person = people[name] # person is itself a dictionary
    template = "Person: {} is {} years old and comes from {}"
    print(template.format(name, person["age"], person["hometown"]))

# Sorting by values is tricker. sorted takes a key parameter
# which can point to a function to pull out part of the value
# you want to sort by.
from operator import itemgetter, attrgetter

just_ages = { "bob": 332,
           "john": 33,
           "wei": 34 }

for name in sorted(just_ages, key = lambda x: just_ages[x]):
    print(name)
