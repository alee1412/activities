for x in range(1,20,2):
    print(x)
print("-----------------------")

words = "Peace"
for letters in words:
    print(letters)

zoo = ["dog", "cat", "bat", "bear"]
for animal in zoo:
    print(animal)

run = "y"
while run == "y":
    print("Hi")
    run = input("To run again. Enter y")

start = 0
while(start <= 100):
    print(start)
    start += 1

words = "Peace"
print(words[::-1])