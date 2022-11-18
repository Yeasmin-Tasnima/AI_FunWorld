# even or odd
num = input("Enter a number: ")
num = int(num)
if num % 2 == 0:
    print("Number is even.")
else:
    print("Number is odd")

print("\n")

# cuisine dish
Bangladesh = ["panta", "ilish"]
India = ["panipuri", "doibora"]
Itali = ["pasta", "pizza"]
dish = input("Enter a dish name: ")
if dish in Bangladesh:
    print("This is Bangladeshi cuisine.")
elif dish in India:
    print("This is Indian cuisine.")
elif dish in Itali:
    print("This is Itali cuisine.")
else:
    print("Sorry !! I do not know the cuisine name. :(")