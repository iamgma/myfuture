# Hobby Book: Dictionaries

#In this activity, you will create and access dictionaries that are based on your own hobbies.

## Instructions

# 1. Create a dictionary to store the following information:
my_info = {
    "name":"Gina Massari",
    "age":31,
    "hobbies":["Travel, Hip Hop, Movies"], 
    "wake_up":{
        "Mon":"7",
        "Tues":"7",
        "Wed":"7",
        "Thurs":"7",
        "Fri":"7",
        "Sat":"10",
        "Sun":"10",}
    } 

my_info["age"]

# Putting -1 takes the last one; -2 would take second to last
my_info["hobbies"][-1]

# Start with the parent --> wake up; child would be days of week

print(my_info["wake_up"]["Thurs"])

for i in range(5):
    print(i)

a_list = [
    "Amanda",
    "Jin",
    "David",
]

a_list[0]

messages = []
for x in a_list:
    messages.append("Hello " + x)

# This will only work in Python 3
messages = ["Hello" + x for x in a_list]


# Your name
# Your age
# A list of a few of your hobbies
# A dictionary that includes a few days and the time you typically wake up on those days

# 2. Print out your name, how many hobbies you have, and a time you typically wake up during the week.