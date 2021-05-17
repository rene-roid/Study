# Changing values of a list
thislist = ["discord", "sports", "gaming"]

# To change the value of a specific item, refer to the index number
thislist[1] = "videogame" # Changes the value "sports" to "videogame"
print(thislist)


# Changing a range of item values
videogames = ["league of legends", "roblox", "raid shadow legends", "brawl stars", "valorant"]

# To change a range of values, refer the range of index numbers and define the list with the new values
videogames[1:3] = ["clash royale", "ninja!"]
print(videogames)


#Inserting items
fruits = ["apple", "bannana", "watermelon"]

# To insert a new list item without replacing any existing values, we can use the insert() method
# Use the insert method and specify where do you want to add your new value and what value you want to add
fruits.insert(2, "melon")
print(fruits)
