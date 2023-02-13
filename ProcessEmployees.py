"""
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
"""

import csv

# open the file
employee = open("employee_data.csv", "r")
employee_file = csv.reader(employee, delimiter=",")
outfile = open("employee_data.csv", "w")

# create an empty dictionary
emp_names = {}

# use a loop to iterate through the csv file
for emp in employee:
    print(employee)

    # check if the employee fits the search criteria
criteria = "employee"

if criteria in emp_names:
    print("fits criteria")
else:
    print("does not fit search criteria")

print()
print("=========================================")
print()

# iternate through the dictionary and print out the key and value as per printout
for emp in employee:
    print(f"Manager Name: ['First Name']['Last Name']", "Current Salary: ['Salary']")
    print("Manager Name: 




outfile.close
