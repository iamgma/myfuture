# Create a variable called 'name' that holds a string
real_name = "Gina Massari"

# Create a variable called 'country' that holds a string
country = "USA"

# Create a variable called 'age' that holds an integer
age = 31

# Create a variable called 'hourly_wage' that holds an integer
hourly_wage = 75

# Calculate the daily wage for the user
daily_wage = hourly_wage * 8


# Create a variable called 'satisfied' that holds a boolean
satisfied = True

# Print out "Hello <name>!"
print("Hello " + real_name + "!" )

# Print out what country the user entered
print(country)
print("You live in the " + country + ".")

# Print out the user's age
print(age)
print("You are " + str(age) + " years old.")

# With an f-string, print out the daily wage that was calculated
print("You make " + str(daily_wage) + " for a day's work.")
print(f"You make {daily_wage} for a day's work.")

# With an f-string, print out whether the users were satisfied
print(f"Were the users satisfied? {satisfied}")