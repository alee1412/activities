import os
import csv

Index = [1,2,3,4]
Employee = ["Adrian", "Eugene", "Rory", "Emma"]
Department = ["Sales", "Boss", "Sales", "HR"]

roster = zip(Index, Employee, Department)
print(roster)
output = os.path.join("output.csv")
with open(output, 'w', newline='') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Index", "Employee", "Department"])
    writer.writerow(roster)

for employee in roster:
    print(employee)