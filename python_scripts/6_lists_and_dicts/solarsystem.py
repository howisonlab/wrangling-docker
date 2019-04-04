import pprint

solarsystem = {   "1" : "O",
                  "2" : "K", 
                  "3" : "B",
                  "Mars" : { "1" : "T",
                             "2" : "M",
                             "Venus" : { "1" : "R",
                                         "2" : "K",
                                         "3" : "D"
                                       },
                             "3" : "W",
                             "Jupiter" : { "1" : "9",
                                           "Pluto" : { "1" : "K",
                                                       "2" : "J" 
                                                     },
                                          },
                            },
                  "4" : "S",
                  "5" : "C"
        } 

pprint.pprint(solarsystem)

# We can reach down into this dict of dicts and pull out parts
print(solarsystem["Mars"]["Jupiter"]["Pluto"]["2"])

# We can also build up a complex structure from smaller parts, using
# intermediate variable names
pluto = { "1" : "K", "2" : "J" }
pprint.pprint(pluto)
jupiter = { "1" : "9", "Pluto" : pluto, "1" : "K", "2" : "J" }
venus = { "1" : "R", "2" : "K", "3" : "D" }
mars = { "1" : "T", "2" : "M", "Venus" : venus, "3" : "W", "Jupiter" : jupiter }
solarsystem2 = { "1" : "O", "2" : "K", "3" : "B", "Mars" : mars, "4" : "S", "5" : "C" }

print("Solarsystem 2")
pprint.pprint(solarsystem2)

