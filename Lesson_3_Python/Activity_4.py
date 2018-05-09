import os
import csv

filepath = os.path.join("Resources", "employees.csv")

new_employee_data = []

#Read data into a dictionary and create an email
with open(filepath, newline="") as csvfile:
    print(csvfile)
    reader = csv.DictReader(csvfile)
    #print(reader)
    for row in reader:
        
        print(row["First Name"])
        first_name = row["First Name"]
        last_name = row["Last Name"]
        email = first_name + "." + last_name + "@example.com"
        #option 2
        #email = f"{first_name}.{last_name}@example.com"
        new_employee_data.append({
            "First Name": first_name,
            "Last Name": last_name,
            "SSN": row["SSN"],
            "email": email
        })
print(new_employee_data)

# Grab the filename from original path
print(filepath)
monkey, filename = os.path.split(filepath)
print(_)
print(filename)

csvpath = os.path.join("output", filename)
with open(csvpath, "w") as csvfile:
    field_names = ["Last Name", "First Name", "SSN", "email"]
    writer = csv.DictWriter(csvfile, fieldnames = field_names)
    writer.writeheader()
    writer.writerow(new_employee_data)

