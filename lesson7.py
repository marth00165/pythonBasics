whatisList = ["A", " List", " Is", " a", " Bunch", " of", " values"]
print(whatisList)
s = ""
print(s.join(whatisList), "\n use the join function to combine all the items in an array together")


stuff = ["chicken", "apples", "oranges", "bread", "fries"]
print("")
print(stuff)
print("")
print(stuff[1:3]) # this prints a range of items
# you can change specific elements 
print("")
stuff[1] = "bananas"
print("")
print(stuff)
# now bananas will replace apples