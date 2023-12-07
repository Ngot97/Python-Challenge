import os
import csv

# Path to collect data from the resource file
csv_path = os.path.join('C:\\Users\\cherr\\OneDrive\\Desktop\\Data Analytics UWA course\\Homework\\Week 3\\Module 3 Challenge\\PyBank\\Resources\\budget_data.csv')

month = []
revenue = []
monthly_change = []

with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    total_revenue = 0
    previous_month_revenue = 0

    for row in csvreader:
        # Total Months
        month.append(row[0])

        # Total revenue
        total_revenue += int(row[1])

        # Monthly Change
        current_month_revenue = int(row[1])
        change = current_month_revenue - previous_month_revenue
        monthly_change.append(change)

        previous_month_revenue = current_month_revenue

# Avg Change
average_change = sum(monthly_change) / len(monthly_change)

# Greatest Increase/Decrease
greatest_increase_profits = max(monthly_change)
greatest_decrease_profits = min(monthly_change)

# Find the index of the greatest increase/decrease to get the corresponding month
month_increase = month[monthly_change.index(greatest_increase_profits)]
month_decrease = month[monthly_change.index(greatest_decrease_profits)]

# Print Statements
print(f'Financial Analysis' + '\n')
print(f'----------------------------' + '\n')
print("Total Months: " + str(len(month)))
print("Total: $ " + str(total_revenue))
print("Average Change: $" + str(round(average_change, 2)))
print(f"Greatest Increase in Profits: {month_increase} (${greatest_increase_profits})")
print(f"Greatest Decrease in Profits: {month_decrease} (${greatest_decrease_profits})")
