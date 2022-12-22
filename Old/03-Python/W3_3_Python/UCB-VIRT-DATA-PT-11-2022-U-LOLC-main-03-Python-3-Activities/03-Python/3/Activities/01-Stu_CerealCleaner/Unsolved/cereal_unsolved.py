# Imported 2 libraries --> os is operating system, that's why using the path.join 
import os
import csv

# This is the path cereal_csv = os.path.join("..", "Resources", "cereal_bonus.csv")

# Right click on cereal.csv --> "Copy Relative Path"
# file_path is a variable --> this variable is a string so used ""
file_path = "01-Stu_CerealCleaner\Resources\cereal_bonus.csv"

# This is a folder so if need to go back in the folder can use ..
# And switch to forward slash bc in windows
# Windows give you back slash but needs to be changed

cereal_csv = "../Resources/cereal_bonus.csv"

# We need to take this file and open it so use function open(what do you want to open)
# The default of opening a file is to read it --> "r"
# Remember if you open something you need to close it

#read = open(cereal_csv, "r")
#read.close()

# Python 3 came up with new logic called "with"
# with will do the opening and the closing without calling read = open(cereal_csv, "r") and read.close()

with open(cereal_csv, "r") as read:
    csv_read = csv.reader(read, delimiter=",")
    print(csv_read)
    for row in csv_read:
        if float(row[3])>100:
            print(float(row[3]))
    #a = 1

# So if you print something outside the above block it will be closed automatically
print("Hi")     

# Right clicked  on cereal_unsolved.py --> Open in Integrated Terminal 
# When that terminal opened --> typed in python .\cereal_unsolved.py