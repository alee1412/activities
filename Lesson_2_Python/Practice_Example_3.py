shopping = 'y'

pie_purchases = []

pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun", "Blueberry", "Buko", "Burek", "Tamale", "Steak"]
print("Welcome House of Pie")

while shopping == 'y':
    print("-----------------------------")
    print("(1) Pecan. (2) Apple Crisp. (3) Bean. (4) Banoffee. (5) Black Bun. (6) Blueberry. (7) Buko. (8) Burek. (9) Tamale. (10) Steak")
    pie_choice = int(input("Which pie would you like? "))
    pie_purchases.append(pie_choice)
    print(pie_choice)
    print("-----------------------------")
    print("Great we'll have that " + pie_list[int(pie_choice - 1)] + " pie right out for you. \nYou're Awesome.")
    shopping = input("Would you like to make another purchase (y)es or (n)o? ")

print("-----------------------------")
print("You purchased a total of " + str(len(pie_purchases))+ ".")
