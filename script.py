inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

#how many items in inventory
inventory_len = len(inventory)


#first item in inventory
first = inventory[0]


#last item in inventory
last=inventory[-1]

#selecting items starting at index 2 up to, but not including, index 6
inventory_2_6 = inventory[2:6]


#first 3 items of inventor
first_3 = inventory[:3]


#total number of 'twin bed'

twin_beds = inventory.count("twin bed")


#removing 5th element from inventory

removed_item = inventory.pop(4)


#adding "19th Century Bed Frame" as the 11th element
inventory.insert(10,"19th Century Bed Frame")


#Using sort
print(inventory.sort())


#Using sorted
print(sorted(inventory))

