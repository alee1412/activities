candy_list = ["Snickers", "Kit-Kat", "Twix", "PayDay", "Skittles", "M&M's"]

allowance = 6

candy_cart = []

for candy in candy_list:
    print("[" + str(candy_list.index(candy)) + "] " + candy )

for x in range(allowance):
    selected = int(input("Which candy would you like to bring home? "))
    candy_cart.append(candy_list[selected])
print("I bought home with me...")
for candy in candy_cart:
    print(candy, end=". ")