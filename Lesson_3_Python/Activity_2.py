
lst = ["A", "B", "C"]

item = {"key": 100}
#dict name key
item2 = {"name": "Albert"}
print(item["key"])
print(item2["name"])

#dictionary can contain multiple pair of information
hero = {"name": "Iron Man", "nationality": "United States", "type": False}

item3= {"bag": ["laptop", "usb", "food"], "pocket": ["5.00", "1.00", 'gum'], 
"reddit": {"key": ["1","2","3","7"]}
}

print(item3["bag"])
print(item3["pocket"])
print(item3["reddit"]["key"][2])

for keys in item3:
    print(keys)
