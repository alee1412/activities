item1 = {"Name": "Albert"}
item2 = {"Age": "26"}
item3 = {"Hobbies": ["Shooting", "Gaming", "Sleeping", "Traveling"]}
item4 = {"Wakeup": ["7:00AM", "9:00AM", "11:00AM"]}

print(item1["Name"])
print(item2["Age"])
print(item3["Hobbies"])

print("------------------------")

Albert = {
    "name": "Albert",
    "age": "26",
    "hobbies": ["Shooting", "Gaming", "Sleeping", "Traveling"],
    "wake_up": {"Mon": "7:00", "Tues": "5:00", "Sat": "9:00"}
}
print("Hello I am " + Albert["name"] + " my age is " + str(Albert["age"]))
for hobby in Albert["hobbies"]:
    print(hobby)
for time in Albert["wake_up"].values():
    #print(time + " " + str(Albert["wake_up"][time]))
    print(time)
for k, v in Albert["wake_up"].items():
    print(k)
    print(v)
