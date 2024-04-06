#BMI is calculated as follows
# weight(kg) / height² (m²)
# write a progamm to calculate the BMI without any decimals

# First I need to find out the hight and weight of the person.
height = float(input("How tall are you in meters? \n"))
weight = int(input("How much do you weight in KG? \n"))

# now to the math mobile
bmi = round(weight / (height**2) , 1)
# Add the rounded int to the print by using an f-string. with f-strings 
# pointy brackets must be used around the variable names to work
#print(f"Your BMI is {bmi}")

# Time vor v2.0. v2.0 means ifs and elses so here goes.

if bmi > 35:
    print(f"Your BMI is {bmi}. You are clinically obese")
elif bmi < 35 and bmi > 30:
    print(f"Your BMI is {bmi}. You are obese")
elif bmi < 30 and bmi > 25:
    print(f"Your BMI is {bmi}. You are slightly overweight")
elif bmi < 25 and bmi > 18.5:
    print(f"Your BMI is {bmi}. You have a normal weight")
else:
    print(f"Your BMI is {bmi}. You are underweight")