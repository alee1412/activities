prices = ["24", "13", "16000", "1400"]
price_nums = [int(price) for price in prices]
print(prices)
print(price_nums)

print("**************************************")

dog = "poodle"
letters = [letter for letter in dog]
print(letters)
print(f"We iterate over a string into a list: {letters}")

print("**************************************")

capital_letters = [letter.upper() for letter in letters]
capital_letters = []
for letter in letters:
    capital_letters.append(letter.upper())
print(capital_letters)

print("**************************************")

#First way
no_o = [letter for letter in letters if letter != 'o']
print(no_o)

#Second way
no_o = []
for letter in letters:
    if letter != 'o':
        no_o.append(letter)
print(no_o)

print("**************************************")

june_temperature = [72,65,59,87]
july_temperature = [87,85,92,79]
august_temperature = [88,77,66,100]
temperature = [june_temperature, july_temperature, august_temperature]

print("**************************************")

#short hand
lowest_summer_temperature = [min(temps) for temps in temperature]
maximum_summer_temperature = [max(temps) for temps in temperature]

print(sum(maximum_summer_temperature)/len(maximum_summer_temperature))
print(lowest_summer_temperature[0])
print(lowest_summer_temperature[1])
print(lowest_summer_temperature[2])

print("=" * 30)

print("**************************************")

#long hand
lowest_summer_temperature = []
for temps in temperature:
    lowest_summer_temperature.append(min(temps))

print(lowest_summer_temperature[0])
print(lowest_summer_temperature[1])
print(lowest_summer_temperature[2])
print(sum(lowest_summer_temperature)/len(lowest_summer_temperature))

print("**************************************")

def name(parameter):
    return "Hello " + parameter
print(name("Albert"))

def average(data1,data2):
    return (sum(data1)/len(data1)) + (sum(data2)/len(data2))
print("=" * 40)
print(average([1,2,3,4,5],[2,3,4,5,6]))