 # Print Hello User!
print("Hello User")

# Take in User Input
name = input("Please enter your name:")

# Respond Back with User Input
print("Nice to meet you, " + name + "!")

# Take in the User Favorite Number
fav_number = input("What is your favorite number?")

# Computer Favorite Number
comp_fav_num = 11

# Respond Back with a statement based on your favorite number
if int(fav_number) == (comp_fav_num):
    print("OMG twinning! That's my favorite number too!")

elif int(fav_number) > (comp_fav_num):
    print("Your favorite number is higher than mine!")

elif int(fav_number) < (comp_fav_num):
    print("Your favorite number is lower than mine!")

# This doesn't work because string not int (but tico says there is something called Try/Accept for this very situation - more advanced Python)
else:
    print("Hey, that's not a number?! C'mon just tell me what you favorite number is!")
