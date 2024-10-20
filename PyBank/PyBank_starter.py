# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("C:\Users\rauts\Downloads\Starter_Code\Starter_Code\PyBank","Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load) as financial_data:
   csv_reader = csv.reader(financial_data, delimiter=',')

    # Skip the header row
   csv_header = next(csv_reader)
   print(f"CSV Header:{csv_header}")

    # Extract first row to avoid appending to net_change_list


    # Track the total and net change


    # Process each row of data
   for row in csv_reader:
        print(row)

        # Track the total


        # Track the net change


        # Calculate the greatest increase in profits (month and amount)


        # Calculate the greatest decrease in losses (month and amount)



# Calculate the average net change across the months


# Generate the output summary


# Print the output


# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
