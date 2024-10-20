# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("..", "Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("..", "analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
previous_value = None
changes = []

# Open and read the csv
with open(file_to_load, encoding='UTF-8') as financial_data:
    csv_reader = csv.reader(financial_data, delimiter=',')

    # Skip the header row
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")

    # Process each row of data
    for row in csv_reader:
        current_value = int(row[1])  
        total_months += 1
        total_net += current_value

        # Track the net change
        if previous_value is not None:
            change = current_value - previous_value
            changes.append(change)

        # Set previous value for the next iteration
        previous_value = current_value

# These print statements should be outside the loop
print(f"Total Months  : {total_months}")
print(f"Total Net : {total_net}")

# Calculate the average net change across the months
if changes:
    average_change = sum(changes) / len(changes)
    print(f"Average change in 'Profit/Losses': {average_change}")
else:
    print("No changes to calculate.")

# Calculate the greatest increase and decrease in profits (month and amount)
if changes:
    greatest_increase = max(changes)
    greatest_decrease = min(changes)
    print(f"Greatest increase in profits: {greatest_increase}")
    print(f"Greatest decrease in profits: {greatest_decrease}")

# Write the results to a text file (optional)
with open(file_to_output, "w") as txt_file:
    txt_file.write(file_to_output)

with open(file_to_output, "w") as txt_file:    # Print and save the total vote count
    financial_analysis = (
        f"Financial Analysis \n"
        f"-------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total : {total_net}\n"
        f"Average Change : {average_change}\n"
        f"Greatest Increase In Profits : {greatest_increase}\n"
        f"Greatest Decrease in Profits : {greatest_decrease}"
    )
    print(financial_analysis, end="")
    txt_file.write(financial_analysis)
