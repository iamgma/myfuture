
def name(parameters):

    return



def show():
    print(f"Hi!")



show()



def show(message):
    print(message)



show("Hello, World!")



def make_quesadilla(protein, topping):
    quesadilla = f"Here is a {protein} quesadilla with {topping}"
    print(quesadilla)



make_quesadilla("beef", "guacamole")
make_quesadilla("chicken", "salsa")


make_quesadilla("sour cream", "beef")



def make_quesadilla(protein, topping="sour cream"):
    quesadilla = f"Here is a {protein} quesadilla with {topping}"
    print(quesadilla)


make_quesadilla("chicken")

make_quesadilla("beef", "guacamole")



def square(number):
    return number * number



squared = square(2)
print(squared)


print(square(2))
print(square(3))
