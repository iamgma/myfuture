try:
    number = int(input ("Enter a number:"))
    print(number)
except:
    print("Invalid Input")



try:
    value = 10/0 
    number = int(input ("Enter a number:"))
    print(number)
except ZeroDivisionError:
    print("Divided by zero, that's a no no!")
except ValueError:
    print("Invalid Input")