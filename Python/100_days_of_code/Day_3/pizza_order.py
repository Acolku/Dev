# make the customer choose the size of the pizza and weather the want 
# to add pepperoni or extra cheese. Pepperoni for S pizza is $2,
# M or L pizza is $3. Extra cheese is always $1 extra

size = input("What size pizza you want? S, M or L\n")
pepperoni = input("Do you want pepperoni? Y or N\n")
cheese = input("Do youm want extra cheese? Y or N\n")

if size =="S":
    price = 15
elif size == "M":
    price = 20
elif size == "L":
    price = 25
if pepperoni =="Y" and size =="S":
    price +=2
if (pepperoni =="Y" and size =="M") or (pepperoni=="Y" and size=="L"):
    price +=3   
if cheese =="Y":
    price +=1
print(f"Your total will be ${price}")