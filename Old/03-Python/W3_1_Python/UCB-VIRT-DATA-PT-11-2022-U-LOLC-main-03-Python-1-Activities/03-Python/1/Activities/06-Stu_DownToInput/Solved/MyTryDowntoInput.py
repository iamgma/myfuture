# Take input of you and your neighbor
my_name = input("What is your name?")
neighbor_name = input("What is your neighbor's name?")

# Take how long each of you have been coding
me_code = input(my_name +", how many months have you been coding?")
neighbor_code = input("How many months has " + neighbor_name + " been coding?")

# Add total month
# Create two more inputs to ask how many months you and your neighbor have been coding.
combined_total_code = int(me_code) + int(neighbor_code)

# Print results
print("You two have been coding for a combined total of" + str(combined_total_code) + " months.")
