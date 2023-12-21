# TODO: take in fellow first name
fname = input("give me your first name:")

# TODO: take in fellow track name
track = input("Please give me your track")

# TODO: take in the names of fellows that they know
name = input("give me the name of the fellows you know")
familiars = []
while name != "exit":
    familiars.append(name)
    name = input("type exit to quit. \n")

# TODO: print out all information
print(fname)
print(track)
print(familiars)
