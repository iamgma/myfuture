import os
import csv

# Path to collect data from the Resources folder
graduation_csv = "../Resources/graduation_data.csv"

# Define the function and have it accept the 'state_data' as its sole parameter
def print_percentages(row): 

# Find the total students
# This is the names starting from 1
    Adjusted_cohort_Public = int(row[1])
    Completers_Public =  int(row[2]) 
    Adjusted_cohort_Nonprofit_Private =  int(row[3])
    Completers_Nonprofit_Private =  int(row[4])
    Adjusted_cohort_Forprofit_Private =  int(row[5]) 
    Completers_Forprofit_Private =  int(row[6])

    total_students = Adjusted_cohort_Public + Adjusted_cohort_Nonprofit_Private + Adjusted_cohort_Forprofit_Private


# Find the total graduates
    total_grads = Completers_Public + Completers_Nonprofit_Private + Completers_Forprofit_Private

# Find the public school graduation rate
    public_grad_rate = (Completers_Public/Adjusted_cohort_Public) * 100

# Remember that some states do not have nonprofit or forprofit private schools
# Find the non-profit school graduation rate
    nonprofit_grad_rate = (Completers_Nonprofit_Private/Adjusted_cohort_Nonprofit_Private) * 100

# Find the for-profit school graduation rate
    forprofit_grad_rate = (Completers_Forprofit_Private/Adjusted_cohort_Forprofit_Private) * 100

# Calculate the overall graduation rate
    overall_grad_rate = (total_grads/total_students) * 100


# Print out the state's name and its graduation rates
# The 2 is for decimal places
    msg = f"""
    State: {row[0].title()}
    public_grad_rate: %{round(public_grad_rate, 2)}
    nonprofit_grad_rate: %{round(nonprofit_grad_rate, 2)}
    forprofit_grad_rate: %{round(forprofit_grad_rate, 2)}
    overall_grad_rate: %{round(overall_grad_rate, 2)}
"""
    return msg

# Read in the CSV file
with open(graduation_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    print(header)

    # # Prompt the user for what state they would like to search for
    state_to_check = input("What state do you want to look for? ")

    # # Loop through the data
    for row in csvreader:

        # If the state's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if state_to_check.lower() == row[0].lower():
            # print_percentages(row)
            print(print_percentages(row))
