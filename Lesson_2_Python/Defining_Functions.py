def printHello():
    print("Hello")
printHello()

print("------------------------------")

def printName(name):
    print("Hello " + name + "!")
printName("Emma")

print("------------------------------")

listOne = [1,2,3,4,5,6,7]
listTwo = [11,12,13,14,15]

def listinfo(lst):
    print("The values within the list are...")
    for value in lst:
        print(value)
    print("length = " + str(len(lst)))

listinfo(listOne)
print("------------------------------")
listinfo(listTwo)
print("------------------------------")
listinfo([1,2,3,4,5])