

print("******************************************************************************")
print("# 1 : LIST")
print("A) ***************************************************************************")
"""
    a) CREATE a list of 5 strings.
    
    b) Print the LAST item in the list. 
        How can you ALWAYS print the last item even if the list grows?
    
    c) ADD '_001' to the last item and overwrite the last item in the original list with the new result.
    
    d) Print the updated last item again.
"""
# A
common_pets = ["Cats", "Dogs", "Birds", "Fish", "Rabbits"]

# B
print (common_pets[-1])

# C
common_pets[-1] = common_pets[-1] + "_001"

# D
print (common_pets[-1])

# Practiced 3 times

print("\n\nB) **************************************************************************")
"""
a) Add a new item to the list from 1A).
b) Delete the first item.
c) Print out the list before and after.
"""
#A
print("Before:" common_pets)

common_pets.append("Reptiles")
print(common_pets)

# B
common_pets.remove("Cats")
print(common_pets)

# C
print("After:" common_pets)

# Practiced

print("\n\n**************************************************************************")
print("# 2 : DICTIONARY")
print("******************************************************************************")
"""
a) CREATE a "user" dictionary with a name, job, permission and tasks which will be filled with content.
b) "tasks" should be filled with a list of 3 asset names: mike, sulley and remy.
c) Print the final result.
"""
# A, B, C
user_dict = {"name" : "Melodi",
             "job" : "Programmer",
             "tasks" : ["mike", "sulley", "remy"] }
print(user_dict)
# Prints Dictionary


user_dict["name"]
print(user_dict["name"])
# Printing a section for the dictionary



print("\n\n******************************************************************************")
print("# 3 : STRING")
print("A) ******************************************************************************")
"""
a) CHANGE the following file_name from s060 to s120
b) CHANGE LGT to LAY
c) REMOVE _pre at the end

CHALLENGE: Can you do it in just 3 lines?
"""
#A
file_name = "s060_LGT_v001_ar_pre.ma"
#B
file_name = file_name.replace("s060", "s120").replace("LGT", "LAY").replace("_pre", "")
# empty strings for removing the characters
#C
print(file_name)




print("\n\nB) **************************************************************************")
"""
UPDATE rig to uppercase RIG using string manipulation.

CHALLENGE: Can you do it with just 1 line?
"""

asset_name = 'mike_001_rig'

asset_name = asset_name.replace("rig", "RIG")

print(asset_name)






print("\n\nC) **************************************************************************")
"""
UPDATE the task at the end of your asset_name to uppercase.
mike_001_lgt -> mike_001_LGT

The script should be flexible enough to uppercase every possible task:
rig, lgt, surf, ... -> RIG, LGT, SURF, ...

TIP: Test your script by changing the asset_name manually from 'lgt' to 'geo'. Is it still uppercase?
"""
#A
asset_name = 'mike_001_lgt'
#B
parts = asset_name.split("_")
parts[-1] = parts[-1].upper()
asset_name = "_".join(parts)





print("\n\n**************************************************************************")
print("# 4 : FIX IT")
print("******************************************************************************")
# COMMENT each block in, build it and fix the problem (do it one at a time).


print("A) ******************************************************************************")
# PRINT string and integer together
"""
selected_assets = 21
print('Selected assets: ' + selected_assets)
"""

# Fixed
print("Selected assets: " + str(selected_assets))




print("\n\nB) **************************************************************************")
# ACCESS user name
"""
user = {"name"    :"John",
        "address" : 'Here',
        "salary"  : 0}

name = user[0]
"""

print(user["name"])





print("\n\nC) **************************************************************************")
# ACCESS the right planets
"""
planet = ["Mars", "Moon", "Earth"]
our_planet = planet[2]
mars = planet[1]
print mars
"""

planet = ["Mars", "Moon", "Earth"]
our_planet = planet[2]
Mars = planet[0]
Moon = planet[1]
Earth = planet[2]
print(planet[0])
print(planet[1])
print(planet[2])
