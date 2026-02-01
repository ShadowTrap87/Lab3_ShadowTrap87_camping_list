"""
Project Name: Replacing Items in Camping List
Author: Kennett Aguilar-Zaldana
Purpose: Replace an item from the camping list with 'binoculars' and to show slice notation
Starter Code: Lab3_ShadowTrap87_add.py
Date: 01/31/26"""

#Import
from Lab3_ShadowTrap87_add import camping_items

#Replace
camping_items[8] = 'Binoculars'

#Slicing
print(f'\n')
for before in camping_items[0:8]:
    print (before)

print(f'\n')
print (camping_items[8])

print(f'\n')
for after in camping_items[9:]:
    print (after)