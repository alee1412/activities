import os
import csv

output_path = os.path.join("new.csv")

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['First Name', 'Last Name', 'Pin'])
    csvwriter.writerow(["Albert", "Lee", "1076"])
