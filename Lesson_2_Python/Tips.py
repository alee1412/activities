a = [1,2,3]
x, y, z = a
print(x)
print(y)
print(z)

print("------------------------------")

a = ["Hello", "World"]
print(" ".join(a))

print("------------------------------")

list1 = ["a", "b", "c"]
list2 = ["1", "2", "3"]
for x,y in zip(list1, list2):
    print(x,y)

print("------------------------------")

a = 8
b = 5
b, a = a, b
print(a)
print(b)
