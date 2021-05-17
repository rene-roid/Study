# To add an item to the end of a list we use the append() method

appendList = ["Hello", "how", "are"]

# Use the append method and then add your value
appendList.append("you?")
print(appendList)

#Inserting items
fruits = ["apple", "bannana", "watermelon"]

# To insert a new list item without replacing any existing values, we can use the insert() method
# Use the insert method and specify where do you want to add your new value and what value you want to add
fruits.insert(2, "melon")
print(fruits)


# Extenging a list
gamingTime = ["1 hour pack", "2 hours pack", "3 hours epic pack"]
gamingGames = ["League of legends" , "Brawl Stars", "Roblox"]

# To extend a list you append it to another existing list using the extend() method, and adding the list you want to add inside the extend(method)
gamingTime.extend(gamingGames)
print(gamingTime)

# You can add any iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)