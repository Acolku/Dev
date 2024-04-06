#BMI is calculated as follows
# weight(kg) / height² (m²)
# write a progamm to calculate the BMI without any decimals

# First I need to find out the hight and weight of the person.
height = float(input("How tall are you in meters? \n"))
weight = int(input("How much do you weight in KG? \n"))

# now to the math mobile
bmi = round(weight / (height**2))
# Add the rounded int to the print by using an f-string. with f-strings 
# pointy brackets must be used around the variable names to work
print(f"Your BMI is {bmi}")