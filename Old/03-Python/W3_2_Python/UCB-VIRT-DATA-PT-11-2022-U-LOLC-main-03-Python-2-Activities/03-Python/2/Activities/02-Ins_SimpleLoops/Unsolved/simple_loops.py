# A For loop moves through a given range of numbers
# If only one number is provided it will loop from 0 to that number
for x in range(10):
    print(x)

# If two numbers are provided then a For loop will loop from the first number up until it reaches the second number
for x in range(20, 30):
    print(x)

# If a list is provided, then the For loop will loop through each element within the list
grocery_list = ["tuna", "milk", "eggs", "lettuce"]
for item in grocery_list:
    print(item)

# A While Loop will continue to loop through the code contained within it until some condition is met
