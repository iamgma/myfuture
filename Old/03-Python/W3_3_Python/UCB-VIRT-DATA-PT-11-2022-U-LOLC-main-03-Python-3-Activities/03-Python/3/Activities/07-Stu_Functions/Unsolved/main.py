# @TODO: Write a function that returns the arithmetic average for a list of numbers
list = range(0, 25, 2)

def average(a_list):
    total = 0
    items = 0
    for x in a_list:
        items = items + 1
        total = total + x
        avg = total/len(a_list) 
    return avg 

# Test your function with the following:

print(average([1, 5, 9]))
print(type(average([1, 5, 9])))
print(average(range(11)))
print(average(list))