"""
Program Name: Camp Packing List
Author: Kennett Aguilar-Zaldana
Purpose: To create a list of items for a camping trip, display the total number of items, and to print the list out alphabetically
Stater Code: None
Date: 01/30/26
"""
#Camping item list
camping_items = ['Tent', 'Sleeping Bag', 'Bug Spray', 'Sunscreen', 'First-Aid Kit', 'Water Bottle', 'Map', 'Lighter', 'Lights', 'Food']

#Item total
print ("The total number of items is:", len(camping_items))

#Alphabetical list
print ("Alphabetically Sorted:")
for item in sorted(camping_items):
    print (item)
